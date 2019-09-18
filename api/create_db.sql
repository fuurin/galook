CREATE TABLE games (
     id SERIAL, -- ゲームを識別するための連番
     title TEXT NOT NULL, -- ゲームタイトル
     brand TEXT, -- ブランド
     story TEXT, -- あらすじ
     standard_edition_id INT REFERENCES editions(id), -- 代表エディションの id
     PRIMARY KEY(id)
 );

 CREATE TABLE editions (
     id INT, -- getchu.com の販売ページ URL などに含まれる ID
     game_id INT,   -- このedition が含まれる game の　ID
     title TEXT NOT NULL, -- edition ごとのタイトル
     brand TEXT, -- ブランド
     story TEXT, -- あらすじ
     price INT, -- 販売価格
     release_date DATE, -- 発売日
     url TEXT, -- edition ごとの販売ページ URL
     PRIMARY KEY(id)
 );
 
 CREATE TABLE categories (
  	edition_id INT REFERENCES editions(id), -- 対象の edition
  	category_name TEXT, -- カテゴリ名
  	PRIMARY KEY(edition_id, category_name)
  );	
 
 CREATE TABLE subgenres (
     edition_id INT REFERENCES editions(id), -- 対象の edition
     subgenre_name TEXT, -- サブジャンル名
     PRIMARY KEY(edition_id, subgenre_name)
 );
 
 CREATE TABLE writers (
  	edition_id INT REFERENCES editions(id), -- 対象の edition
  	writer_name TEXT, -- ライター名
  	PRIMARY KEY(edition_id, writer_name)
 );
 
 CREATE TABLE similar_games (
     game_id INT REFERENCES games(id),	-- 対象のゲームの ID
     similar_game_id INT REFERENCES games(id),  -- 対象のゲームに似たゲームの ID
     rank INT, -- 何番目に似ているか
     similarity DOUBLE PRECISION, -- 類似度
     PRIMARY KEY(game_id, similar_game_id)
 );