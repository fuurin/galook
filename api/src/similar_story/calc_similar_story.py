from gensim.models import KeyedVectors

import sys
sys.path.append('..')
from db_util import connect_database, execute_sql

vectors_files = [
    'story_vectors.vec', 
    # 'story_vectors_oov_001.vec',
    # 'story_vectors_oov_0001.vec', 
    'story_vectors_wo_ne.vec'
]

for vectors_file in vectors_files:
    vectors = KeyedVectors.load(vectors_file)
    conn = connect_database()

    similar_game_ids = vectors.similar_by_word('9488', topn=10)
    for similar_game_id,cos in similar_game_ids:
        curs = execute_sql(conn, "SELECT id, title, story FROM games WHERE id=%s;", (similar_game_id,))
        for row in curs:
            print(row[:2], cos)
    print()