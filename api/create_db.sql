CREATE TABLE games (
     id INT, -- ゲームを識別するための連番
     title TEXT NOT NULL, -- ゲームタイトル
     brand TEXT, -- ブランド
     story TEXT, -- あらすじ
     standard_edition_id INT REFERENCES editions(id), -- 代表エディションの id
     PRIMARY KEY(id)
 );

CREATE TABLE editions (
    id INT, 
    game_id INT REFERENCES games(id), 
    title TEXT NOT NULL,
    brand TEXT,
    story TEXT,
    price INT,
    release_date DATE,
    url TEXT, 
    PRIMARY KEY(id)
);

CREATE TABLE categories (
 	edition_id INT REFERENCES editions(id),
 	category_name TEXT,
 	PRIMARY KEY(edition_id, category_name)
 );	

CREATE TABLE subgenres (
    edition_id INT REFERENCES editions(id),
    subgenre_name TEXT,
    PRIMARY KEY(edition_id, subgenre_name)
);

CREATE TABLE writers (
 	edition_id INT REFERENCES editions(id),
 	writer_name TEXT,
 	PRIMARY KEY(edition_id, writer_name)
);

CREATE TABLE similar_games (
    game_id INT REFERENCES games(id),
    similar_game_id INT REFERENCES games(id), 
    rank INT, 
    similarity DOUBLE PRECISION, 
    PRIMARY KEY(game_id, similar_game_id)
);
