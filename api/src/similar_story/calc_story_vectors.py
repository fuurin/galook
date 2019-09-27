import os
import numpy as np
import fasttext
import MeCab
from gensim.models import KeyedVectors
from swem import SWEM

import sys
sys.path.append('..')
from db_util import connect_database, execute_sql


def normalize(v):
    return v / np.linalg.norm(v)


vectors_path = os.getenv('WORD_VECTORS_PATH')
vectors = fasttext.load_model(vectors_path)
neologd_path = os.getenv('NEOLOGD_PATH')
tokenizer = MeCab.Tagger(f"-d {neologd_path}")
swem = SWEM(vectors, tokenizer, stop_pos=('助詞', '助動詞', '記号', '固有名詞'))

conn = connect_database()

curs = execute_sql(conn, "SELECT id, title, story FROM games WHERE CHAR_LENGTH(story) >= 1;")
vectors = KeyedVectors(vector_size=100)
for row in curs:
    game_id, title, story = row
    vectors[str(game_id)] = swem.aver_pooling(story)
    vectors[str(game_id)] = normalize(vectors[str(game_id)])

vectors.save('story_vectors_wo_ne.vec')