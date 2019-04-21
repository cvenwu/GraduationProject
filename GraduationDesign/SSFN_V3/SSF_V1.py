import numpy as np

from SSFN_V3 import util


Sen1_word = []  # 存储句子1的各个单词
Sen2_word = []  # 存储句子2的各个单词
Sen1_word_vec_set = []  # 存储句子1的词向量集合
Sen2_word_vec_set = []  # 存储句子2的词向量集合

S_sen1_vec_set = []  # 存储相对于句子1的相似元对应的词向量，也就是包括在句子1中的相似元对应的词向量
NS_sen1_vec_set = []  # 存储相对于句子1的非相似元对应的词向量
S_sen2_vec_set = []  # 存储相对于句子2的相似元对应的词向量，也就是包括在句子2中的相似元对应的词向量
# NS_sen2_vec_set = []  # 存储相对于句子2的非相似元对应的词向量，也就是包括在句子2中的非相似元对应的词向量
S_sen1_word = []  # 存储相对于句子1的相似元对应的词，也就是包括在句子1中的相似元对应的词
NS_sen1_word = []  # 存储相对于句子1的相似元对应的词，也就是包括在句子1中的相似元对应的词
S_sen2_word = []  # 存储相对于句子1的相似元对应的词，也就是包括在句子1中的相似元对应的词
NS_sen2_word = []  # 存储相对于句子1的相似元对应的词，也就是包括在句子1中的相似元对应的词
u = []  # 存储相似度的集合，如果不相似写入0
U = []  # 只存储相似度非0的集合
# U_word = []  # 存储相似的单词
maxsim = 0

X = []
Y = []


def init(Sen1, Sen2):
    """
    初始化各个参数：包括
                    Sen1_word
                    Sen2_word
                    Sen1_word_vec_set
                    Sen2_word_vec_set
    :param Sen1: 句子1的字符串形式
    :param Sen2: 句子2的字符串形式
    :return:
    """
    global Sen1_word
    global Sen2_word
    global Sen1_word_vec_set
    global Sen2_word_vec_set
    Sen1_word = Sen1.strip().split(' ')
    Sen2_word = Sen2.strip().split(' ')
    Sen1_word_vec_set = util.get_sen_vec_set(Sen1_word)
    Sen2_word_vec_set = util.get_sen_vec_set(Sen2_word)


def calc_simi_element(Sa, Sb, Sa_vec, Sb_vec, u0=0.25):
    """
    计算相似元
    :param Sa: 句子A字符串列表
    :param Sb: 句子B字符串列表
    :param Sa_vec: 句子A对应的词向量集合
    :param Sb_vec: 句子B对应的词向量集合
    :param u0: 相似度阈值, 默认为0.25，判断是否相似，超过阈值认为相似
    :return: None
    """
    global S_sen1_vec_set
    global NS_sen1_vec_set
    global S_sen2_vec_set
    # global NS_sen2_vec_set
    global S_sen1_word
    global NS_sen1_word
    global S_sen2_word
    global NS_sen2_word
    global u
    global U
    global maxsim
    for i in range(len(Sa)):
        maxsim = 0
        for j in range(len(Sb)):
            tmp_sim = util.calc_cos_sim(Sa_vec[i], Sb_vec[j])
            if tmp_sim > maxsim:
                maxsim = tmp_sim
                tmp_word_b = Sb[j]
                tmp_word_b_vec = Sb_vec[j]
        if maxsim > u0:
            S_sen1_vec_set.append(Sa_vec[i])
            S_sen1_word.append(Sa[i])
            S_sen2_vec_set.append(tmp_word_b_vec)
            S_sen2_word.append(tmp_word_b)
            u.append(maxsim)
            U.append(maxsim)
        else:
            NS_sen1_vec_set.append(Sa_vec[i])
            NS_sen1_word.append(Sa[i])
            u.append(0)
    NS_sen2_word = list(set(Sb) - set(S_sen2_word))

def init_set():
    """
    初始化集合X和Y
    :return:
    """
    global Sen1_word
    global Sen2_word
    global S_sen1_word
    global NS_sen2_word
    m = len(Sen1_word)
    n = len(Sen2_word)
    p = len(S_sen1_word)
    N = m + n
    for i in range(N):
        # 初始化集合X
        if i < m:
            X.append(util.get_word_weight(Sen1_word[i], Sen1_word))
        else:
            X.append(0)

        # 初始化集合Y
        if i < p:
            Y.append(util.get_word_weight(S_sen1_word[i], Sen1_word) * U[i])
        elif i < (m + p):
            Y.append(0)
        else:
            Y.append(util.get_word_weight(NS_sen2_word[i-m-p], Sen2_word))


def calc_sen_simi():
    """
        计算两个句子的相似性
        :return: similarity 两个句子的相似性
    """
    global X
    global Y
    p = len(S_sen1_word)
    m = len(Sen1_word)
    tmp_array = np.sum(np.array(Y[:p]))  # 相似度函数的分子
    tmp = np.sqrt(np.sum(np.square(np.array(X[:m]))))  # 相似度函数的分母左半部分

    tmp_right_left = 0.0
    for i in range(p):
        tmp_right_left += ((U[i] ** 2) * (util.get_word_weight(S_sen1_word[i], Sen1_word) ** 2))
    tmp_right = np.sqrt(tmp_right_left + np.sum(np.square(np.array(Y[m+p:]))))
    similarity = tmp_array / (tmp * tmp_right)
    """
    调试使用
    # print("分子：", tmp_array)
    # print("分母左半部分：", tmp)
    # print("分母右半部分：", tmp_right)
    """

    return similarity
