import csv
import pickle
import fasttext
import MeCab
from gensim.models import KeyedVectors
from SWEM import SWEM

vectors_path = "../word_vector/getchu_vector.bin"
vectors = fasttext.load_model(vectors_path)
tokenizer = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
swem = SWEM(vectors, tokenizer)

vectors = KeyedVectors(vector_size=100)
reader = csv.reader(open('../data/data_uniq.csv', 'r'))
next(reader)
index = 0
for row in reader:
    story = row[2].strip()
    if not story:
        continue
    vectors[str(index)] = swem.aver_pooling(story)
    if index % 100 == 0:
        print(index)
    index += 1

vectors.save('story_vector.vec')