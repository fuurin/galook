import json, requests, urllib
from bs4 import BeautifulSoup

# サンプルデータの画像URLを取得したPythonコードです．
# 以下を参考にしてみてはいかがでしょうか．
# 参考：https://qiita.com/naz_/items/efc296ae1bf0e62f6704

keyword = "お兄ちゃん、右手の使用を禁止します！"

GOOGLE_SEARCH_URL = "https://www.google.co.jp/search"
session = requests.session()
session.headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0"})
params = urllib.parse.urlencode({"q": keyword, "tbm": "isch", "ijn": 0})
query = f"{GOOGLE_SEARCH_URL}?{params}"

print(query)

html = session.get(query).text
soup = BeautifulSoup(html, "html.parser")
elements = soup.select(".rg_meta.notranslate")
jsons = [json.loads(e.get_text()) for e in elements]
image_url_list = [js["ou"] for js in jsons]

print(image_url_list[0])