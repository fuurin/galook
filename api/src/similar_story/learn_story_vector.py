import csv
import pickle
import fasttext
import MeCab
from gensim.models import KeyedVectors
from SWEM import SWEM

# タイトルと番号の結びつき
# title_to_index = dict()
# index_to_title = dict()
# reader = csv.reader(open('../data/data_uniq.csv', 'r'))
# next(reader)
# index = 0
# for row in reader:
#     if not row[2].strip():
#         continue
#     title = row[4]
#     title_to_index[title] = str(index)
#     index_to_title[str(index)] = title
#     index += 1
# pickle.dump(title_to_index, open('title_to_index.pkl', 'wb'))
# pickle.dump(index_to_title, open('index_to_title.pkl', 'wb'))
title_to_index = pickle.load(open('title_to_index.pkl', 'rb'))
index_to_title = pickle.load(open('index_to_title.pkl', 'rb'))

vectors_path = "../word_vector/getchu_vector.bin"
vectors = fasttext.load_model(vectors_path)
tokenizer = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
swem = SWEM(vectors, tokenizer)
# vectors = KeyedVectors(vector_size=100)
# reader = csv.reader(open('../data/data_uniq.csv', 'r'))
# next(reader)
# index = 0
# for row in reader:
#     story = row[2].strip()
#     if not story:
#         continue
#     vectors[str(index)] = swem.aver_pooling(story)
#     if index % 100 == 0:
#         print(index)
#     index += 1

# vectors.save('story_vector.vec')

vectors = KeyedVectors.load('story_vector.vec')

titles = (
    '9-nine-そらいろそらうたそらのおと', 
    'BALDR SKY Dive1 新装版', 
    'バタフライシーカー', 
    '11eyes−罪と罰と贖いの少女−', 
    'Dearest Blue', 
    'euphoria', 
    '抜きゲーみたいな島に住んでる貧乳はどうすりゃいいですか？ 通常版', 
)

for title in titles:
    results = vectors.similar_by_word(title_to_index[title], topn=20)
    print(title + 'に似たゲーム')
    for result in results:
        print(result[0], index_to_title[result[0]], result[1])
    print()
    
mytext = "たくさんの妹ができて，ハーレム生活"
results = vectors.most_similar(positive=[swem.aver_pooling(mytext)], topn=20)
for result in results:
    print(result[0], index_to_title[result[0]], result[1])
print()