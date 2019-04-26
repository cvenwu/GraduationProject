from SSFN_V6 import Word2Vec
import nltk


def load_model():
    """
    加载已经训练好的词向量文件
    :return:  加载文件后得到的word2vec模型
    """
    glob_model = Word2Vec.Word2Vec("D:\GoogleNews-vectors-negative300.bin")
    return glob_model


def sen_process(Sen):
    """
    对句子进行预处理以及分词
    :param Sen:
    :return: 返回句子进行预处理和分词后的结果
    """
    return nltk.word_tokenize(Sen)


def get_word_times(word, Sen):
    """
    统计word在sen出现的次数
    :param word: 要统计的单词，是一个字符串
    :param Sen: 句子， 是一个字符串列表
    :return: 返回该单词在句子中出现的次数
    """
    times = 0
    for i in Sen:
        if word == i:
            times += 1
    return times


def get_word_weight(word, Sen):
    """
     统计word的权重 = 在句子中出现的次数 / 句子的长度
    :param word: 要获得权重的单词，单词是一个字符串
    :param sen: 句子，是一个字符串列表
    :return: 返回该单词的权重
    """
    weight = float(get_word_times(word, Sen)) / len(Sen)
    return weight


def get_sen_vec_set(model, sen):
    sen_vec_set = []
    for word in sen:
        sen_vec_set.append(model.get_word_vector(word))
    return sen_vec_set


if __name__ == "__main__":
    print(sen_process("I like china"))