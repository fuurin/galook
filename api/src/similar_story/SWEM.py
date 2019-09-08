import numpy as np


class SWEM:
    OOV_MIN = -0.01
    OOV_MAX = 0.01
    
    def __init__(self, w2v, tokenizer):
        self.w2v = w2v
        self.tokenizer = tokenizer
        self.vocab = set(w2v.words)
        self.dim = w2v.get_dimension()

    def __initialize_oov(self):
       return np.random.uniform(SWEM.OOV_MIN, SWEM.OOV_MAX, self.dim)

    def __get_word_vectors(self, text):
        words = self.tokenizer.parse(text).split('\n')
        vectors = []
        for word in words:
            try:
                surf,detail = word.split('\t')
                pos,*_ = detail.split(',')
                if surf in self.vocab and pos not in ('助詞', '助動詞', '記号' '固有名詞'):
                    vectors.append(self.w2v[surf])
                else:
                    vectors.append(self.__initialize_oov())
            except:
                pass
        return vectors

    def aver_pooling(self, text):
        vectors = self.__get_word_vectors(text)
        return np.mean(vectors, axis=0)

    def max_pooling(self, text):
        vectors = self.__get_word_vectors(text)
        return np.max(vectors, axis=0)

    def hier_pooling(self, text, window_size=2):
        word_vectors = self.__get_word_vectors(text)
        vectors = []
        for i in range(len(word_vectors)-window_size):
            vectors.append(np.mean(word_vectors[i:i+window_size], axis=0))
        return np.max(vectors, axis=0)

    

if __name__ == '__main__':
    import fasttext
    import MeCab

    vectors_path = "../word_vector/getchu_vector.bin"
    vectors = fasttext.load_model(vectors_path)
    tokenizer = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

    swem = SWEM(vectors, tokenizer)
    butterfly_seeker = "舞台は北国の都会、白織市。夏は霧に、冬は雪に煙るこの広大な街は、逸脱した心理に起因する凶悪な犯罪に悩まされてきた。警察署内に「異常心理犯罪対策班」を設立するが、それでも追いつかず、最近では有望な学生を極秘裏に「学生捜査員」として抱えこむまでに至っていた。市立白織学園の昆虫美食部、通称「ムシクイ」も、そうして設けられた学生捜査員たちのユニットである。人の仕草や言動から深く心理を読みとる天童優衣。文字情報の暗記力に優れ、プロファイラーを目指す氷室千歳。高い身体能力を生かして犯罪者と対決する早乙女羽矢。そして、死の遠因を視る特殊能力「バタフライ・シーカー」の持ち主、遠野圭介。遠野の超自然的な力に部員たちの特性が加わり、「ムシクイ」はそれなりの成果をあげていた。そんな折り、遠野たちのもとにある報せが届く。それは、過去に市を震撼させた大量殺人犯「蜘蛛」が6年の時を経て再び活動を開始した、というものだった。"
    print(swem.aver_pooling(butterfly_seeker))
    print(swem.max_pooling(butterfly_seeker))
    print(swem.hier_pooling(butterfly_seeker))