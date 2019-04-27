def wj_similarity(word2vec, sentence1words, sentence2words):
    """
    计算句子的WMD距离
    :param word2vec:  Word2Vec对象
    :param sentence1words:  句子1词语列表
    :param sentence2words:  句子2词语列表
    :return: 两个句子的wj相似度
    """
    return word2vec.sentence_similarity(sentence1words, sentence2words)
