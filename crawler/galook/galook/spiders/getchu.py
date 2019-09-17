# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from galook.items import Game
import urllib.parse
import datetime


field_dict = {
    'ID': 'id', 
    'ブランド': 'brand', 
    'シナリオ': 'writer',
    'サブジャンル': 'subgenre', 
    'カテゴリ': 'category', 
    'ストーリー': 'story',
    '定価': 'price',
    '発売日': 'release_date'
}


class GetchuSpider(scrapy.Spider):
    name = 'getchu'
    allowed_domains = ['getchu.com']

    def __init__(self, end_year, end_month, start_year=1990, start_month=1):
        self.start_urls = [f'http://www.getchu.com/all/price.html?aurl=http://www.getchu.com/all/price.html?genre=pc_soft&gage=adult&month={end_month}&year={end_year}&genre=pc_soft&gc=gc']
        self.end_year = end_year
        self.end_month = end_month
        self.start_year = start_year
        self.start_month = start_month

    def parse(self, response):
        """
        月ごとの発売ゲーム一覧ページのパーズ
        """
        for game_link in response.css('form[name="form2"] td[align="left"]'):
            # 各ゲームの情報取得
            if game_link.css('a'):
                url = game_link.css('a::attr(href)').extract_first().strip()
                url = response.urljoin(url)
                yield SplashRequest(url, callback=self.parse_game)

        older_url = response.css('.charanum ul li a::attr(href)').extract_first().strip()
        if not older_url:
            return
        older_url = response.urljoin(older_url)
        
        # end_year年end_month月より前はクローリング対象外
        url_params = urllib.parse.parse_qs(older_url)
        year = int(url_params['year'][0])
        month = int(url_params['month'][0])
        if year < self.start_year or (year == self.start_year and month < self.start_moth):
            return  

        yield scrapy.Request(older_url)


    def parse_game(self, response):
        """
        ゲームごとの紹介ページのパーズ
        """
        data = {}
        for field in field_dict.values():
            data[field] = ''

        # title, url の情報を抽出
        data['title'] = response.css('h1#soft-title::text').extract_first().strip()
        data['url'] = response.url
        data['id'] = int(response.url.split('=')[1])

        # brand, writer, subgenre, category の情報を抽出
        table = response.css('table[style="padding:1px;"][width="100%"]')
        tbody = table.css('tbody')
        for tr in table.css('tr'):
            # field_name を抽出し，保存対象かどうかを確かめる
            field_name_jn_raw = tr.css('td::text').extract_first()
            if not field_name_jn_raw:
                continue
            field_name_jn = field_name_jn_raw.strip().strip('：').strip()
            if field_name_jn not in field_dict:
                continue
            field_name = field_dict[field_name_jn]

            field_values_text = tr.css('td::text').extract()
            field_values = []
            for text in field_values_text:
                field_values += text.strip().split('、')
            field_values += tr.css('td a::text').extract()
            # field_values には field_name に対応する文字列も一緒に抽出されている
            field_values = list(map(lambda s: s.strip(), field_values))
            field_values = [value for value in field_values if value not in ('', '、', field_name_jn_raw)]
            if field_name == 'brand':
                field_value = ','.join([value for value in field_values if value != '（このブランドの作品一覧）'])
            elif field_name == 'writer':
                field_value = field_values
            elif field_name == 'subgenre' or field_name == 'category':
                field_value = [value for value in field_values if value != '[一覧]']
            elif field_name == 'price':
                field_value = int(field_values[0].replace(',', '').split('(')[0][1:])
            elif field_name == 'release_date':
                year, month, day = map(int, field_values[0].split('/'))
                field_value = datetime.date(year, month, day);

            data[field_name] = field_value

        # story の情報を抽出
        # どの tabletitle_id にストーリーが割り当たっているかはページによる
        for tabletitle_id in range(1, 6):
            tabletitle = response.css(f'.tabletitle_{tabletitle_id}::text').extract_first()
            # startswith('ストーリー') だと <学園編> ストーリー みたいなのを見逃す (例: BALDR SKY Dive 1)
            if tabletitle and 'ストーリー' in tabletitle:
                story_body = response.css(f'.tabletitle_{tabletitle_id} + .tablebody')
                story_text = story_body.css('::text').extract()
                field_value = ''.join(list(map(lambda s: s.strip(), story_text)))
                field_value = field_value.replace('\r', '').replace('\n', '')
                # ストーリーが複数に別れて書かれている時用の区切り処理
                if data['story'] and data['story'][-1] not in ('。', '!', '?', '！', '？'):
                    data['story'] += '。'
                data['story'] += field_value

        yield Game(**data)
