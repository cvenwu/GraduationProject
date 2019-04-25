import numpy as np
import time
import sys
import json
import pymysql
from DBUtils.PooledDB import PooledDB
#5为连接池里的最少连接数
pool = PooledDB(pymysql, 5, host='localhost', user='root', passwd='', db='shop', port=3306)


def get_data_file_path():
    """
    从config.json文件中获得词向量文件的路径以及文件名，然后拼接并返回，便于读取数据
    :return: 返回文件所在的路径 + 文件名
    """
    with open('../config.json', 'r', encoding='utf-8') as f:
        content_dict = json.load(f)
        file_path = content_dict['path']
        file_name = content_dict['name']
    file = file_path + file_name
    return file


def get_word_vec(word):
    """
    计算词在glove文件中对应的词向量
    :param word: 要计算词向量的单词
    :return: 该单词对应的词向量
    """
    vec = []
    print("开始寻找 %s" % word)
    start_time = time.time()
    with open(get_data_file_path(), 'r', encoding='utf-8') as file:
        for i in file.readlines():
            array = i.strip().split(' ')
            if str.lower(word) != str.lower(array[0]):
                continue
            elif str.lower(word) == str.lower(array[0]):
                vec = array[1:]
                end_time = time.time()
                print("已经找到%s，共花费%f秒" % (word, end_time - start_time))
                break
        # 当没有找到单词对应的词向量的时候自动退出，可能用户输入有错误
        if len(vec) == 0:
            print('没有找到 %s 对应的词向量' % word)
            sys.exit(-1)
    return vec


def get_sen_vec_set(S):
    """
    返回句子A所有的词的词向量构成的集合
    :param S: 句子A的字符串列表，不带最后的一个标点
    :return: 返回句子A所有的词的词向量构成的集合
    """
    vec_set = []
    for word in S:
        vec_set.append(get_word_vec(word))
    return vec_set


def calc_cos_sim(word_vec1, word_vec2):
    """
    求两个词向量的余弦距离
    :param word_vec1: 单词1对应的200维度词向量
    :param word_vec2: 单词2对应的200维度词向量
    :return: 两个词向量的余弦距离
    """
    # 转换为numpy数组
    word_vec1 = np.array(word_vec1, dtype=np.float64)
    word_vec2 = np.array(word_vec2, dtype=np.float64)
    # 矩阵乘法求得两个向量的点积
    value = np.dot(word_vec1, word_vec2.T)
    value = value / (np.linalg.norm(word_vec1) * np.linalg.norm(word_vec2))
    return value


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


# print(2 / np.sqrt(8))
# print(calc_cos_sim([1, 1, 2, 1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 1, 1, 1, 1, 1]))
# print(2 / np.sqrt(6))
# print(calc_cos_sim([1, 0, 1], [1, 1, 1]))