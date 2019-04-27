import nltk
import json
from SSFN_V6_02.Methods import Word2Vec
import os
import sys

def model_path():
    """
    根据config.json文件获取预训练模型存储的路径
    :return: 模型对应的路径
    """
    print("000")
    print(os.getcwd())
    print(sys.argv[0])
    with open("D:\git仓库\GraduationProject\GraduationDesign\config.json", 'r') as f:
        print("456")
        return json.load(f)['model_path']


def data_path():
    """
    根据config.json文件获取数据集存储的路径
    :return: 数据集对应的路径
    """
    with open("D:\git仓库\GraduationProject\GraduationDesign\config.json", 'r') as f:
        return json.load(f)['dataset_path']


def load_model():
    """
    加载已经训练好的模型
    :return:  加载文件后得到的word2vec模型
    """
    print("789")
    glob_model = Word2Vec.Word2Vec(model_path())
    return glob_model


def sen_process(sen):
    """
    对句子进行预处理以及分词
    :param sen: 要进行预处理和分词的句子
    :return: 返回句子进行预处理和分词后的结果(列表形式)
    """
    return nltk.word_tokenize(sen)


def is_legal_sent(sen):
    """
    判断用户输入的句子是否合法
    :param sen: 要判断的句子
    :return:    合法 True
                非法  False
    """
    if sen.strip() == '':
        return False
    return True


def get_word_times(word, sen):
    """
    统计word在sen出现的次数
    :param word: 要统计的单词，是一个字符串
    :param sen: 句子， 是一个字符串列表
    :return: 返回该单词在句子中出现的次数
    """
    times = 0
    for i in sen:
        if word == i:
            times += 1
    return times


def get_word_weight(word, sen):
    """
     统计word的权重 = 在句子中出现的次数 / 句子的长度
    :param word: 要获得权重的单词，单词是一个字符串
    :param sen: 句子，是一个字符串列表
    :return: 返回该单词的权重
    """
    weight = float(get_word_times(word, sen)) / len(sen)
    return weight


def get_sen_vec_set(model, sen):
    """
    获得句子的向量集，句子向量是一个列表，每个元素又是对应单词的词向量
    :param model: 对应的模型
    :param sen: 要获得向量集的句子
    :return: 句子的向量集
    """
    sen_vec_set = []
    for word in sen:
        sen_vec_set.append(model.get_word_vector(word))
    return sen_vec_set


if __name__ == "__main__":
    print(model_path())
    print(data_path())
