import numpy as np
from SSFN_V6_02.util import util

Sen1_word = []  # 存储句子1的各个单词
Sen2_word = []  # 存储句子2的各个单词
Sen1_word_vec_set = []  # 存储句子1的词向量集合
Sen2_word_vec_set = []  # 存储句子2的词向量集合
S_sen1_vec_set = []  # 存储相对于句子1的相似元对应的词向量，也就是包括在句子1中的相似元对应的词向量
NS_sen1_vec_set = []  # 存储相对于句子1的非相似元对应的词向量
S_sen2_vec_set = []  # 存储相对于句子2的相似元对应的词向量，也就是包括在句子2中的相似元对应的词向量
S_sen1_word = []  # 存储相对于句子1的相似元对应的词，也就是包括在句子1中的相似元对应的词
NS_sen1_word = []  # 存储相对于句子1的相似元对应的词，也就是包括在句子1中的相似元对应的词
S_sen2_word = []  # 存储相对于句子1的相似元对应的词，也就是包括在句子1中的相似元对应的词
NS_sen2_word = []  # 存储相对于句子1的相似元对应的词，也就是包括在句子1中的相似元对应的词
u = []  # 存储相似度的集合，如果不相似写入0
U = []  # 只存储相似度非0的集合
maxsim = 0

X = []
Y = []


def clear_list():
    """
    如果计算两个句子的相似度之前，如下不为空，则清除列表中的全部内容
                Sen1_word
                Sen2_word
                Sen1_word_vec_set
                Sen2_word_vec_set
                S_sen1_vec_set
                NS_sen1_vec_set
                S_sen2_vec_set
                S_sen1_word
                NS_sen1_word
                S_sen2_word
                NS_sen2_word
                u
                U
                X
                Y
    :return: None
    """
    global Sen1_word
    global Sen2_word
    global Sen1_word_vec_set
    global Sen2_word_vec_set
    global S_sen1_vec_set
    global NS_sen1_vec_set
    global S_sen2_vec_set
    global S_sen1_word
    global NS_sen1_word
    global S_sen2_word
    global NS_sen2_word
    global u
    global U
    global X
    global Y
    global maxsim
    Sen1_word.clear()
    Sen2_word.clear()
    Sen1_word_vec_set.clear()
    Sen2_word_vec_set.clear()
    S_sen1_vec_set.clear()
    NS_sen1_vec_set.clear()
    S_sen2_vec_set.clear()
    S_sen1_word.clear()
    NS_sen1_word.clear()
    S_sen2_word.clear()
    NS_sen2_word.clear()
    u.clear()
    U.clear()
    X.clear()
    Y.clear()
    maxsim = 0


def init(model, Sen1, Sen2):
    """
    初始化各个参数：包括
                    Sen1_word
                    Sen2_word
                    Sen1_word_vec_set
                    Sen2_word_vec_set
    :param model: 预先加载好的模型
    :param Sen1: 句子进行预处理和分词后的列表
    :param Sen2: 句子进行预处理和分词后列表
    :return:        1 初始化成功，也就是所有单词的词向量全部找到
                    0 初始化失败，部分单词的词向量没有找到
    """
    print("初始化开始")
    global Sen1_word
    global Sen2_word
    global Sen1_word_vec_set
    global Sen2_word_vec_set
    Sen1_word = Sen1
    Sen2_word = Sen2
    Sen1_word_vec_set = util.get_sen_vec_set(model, Sen1)
    Sen2_word_vec_set = util.get_sen_vec_set(model, Sen2)
    print("初始化完成")


def calc_simi_element(model, Sa, Sb, Sa_vec, Sb_vec, u0=0.25):
    """
    计算相似元
    :param model: 预先加载好的模型
    :param Sa: 句子A字符串列表
    :param Sb: 句子B字符串列表
    :param Sa_vec: 句子A对应的词向量集合
    :param Sb_vec: 句子B对应的词向量集合
    :param u0: 相似度阈值, 默认为0.25，判断是否相似，超过阈值认为相似
    :return: None
    """
    global S_sen1_vec_set
    global S_sen1_word
    global S_sen2_vec_set
    global S_sen2_word
    global u
    global U
    global NS_sen1_vec_set
    global NS_sen1_word
    global NS_sen2_word
    print("开始计算相似元")
    global maxsim
    for i in range(len(Sa)):
        maxsim = 0
        print("i : ", i)
        for j in range(len(Sb)):
            print("j : ", j)
            print(Sa[i], Sb[j])
            tmp_sim = model.word_similarity(Sa[i], Sb[j])
            print(Sa[i], Sb[j])
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
    print("相似元计算结束")
    NS_sen2_word = list(set(Sb) - set(S_sen2_word))
    print("句子1的相似元：{0}".format(S_sen1_word))
    print("句子2的相似元：{0}".format(S_sen2_word))
    print("句子1的非相似元：{0}".format(NS_sen1_word))
    print("句子2的非相似元 {0}".format(NS_sen2_word))


def init_set():
    """
    初始化集合X和Y
    :return:
    """
    global X
    global Y
    global S_sen1_vec_set
    global S_sen1_word
    global S_sen2_vec_set
    global S_sen2_word
    global u
    global U
    global NS_sen1_vec_set
    global NS_sen1_word
    global NS_sen2_word
    print("初始化X和Y集合")
    m = len(Sen1_word)
    n = len(Sen2_word)
    p = len(S_sen1_word)
    q = len(NS_sen2_word)
    N = m + n
    print("N")
    print(N)
    print(m)
    print(n)
    for i in range(N):
        # 初始化集合X
        if i < m:
            X.append(util.get_word_weight(Sen1_word[i], Sen1_word))
        else:
            X.append(0)

        # 初始化集合Y
        if i < p:
            Y.append(util.get_word_weight(S_sen1_word[i], Sen1_word) * U[i])
        elif i < (N - q):
            Y.append(0)
        else:
            Y.append(util.get_word_weight(NS_sen2_word[i - N + q], Sen2_word))
    print("初始化X和Y完成")
    print(S_sen1_word)


def calc_sen_simi(model, Sen1, Sen2):
    """
    计算并返回两个句子的相似度
    :param model: 预先加载好的模型
    :param Sen1: 预处理和分词之后的句子1
    :param Sen2: 预处理和分词之后的句子2
    :return: 两个句子的相似度
    """
    global X
    global Y
    global S_sen1_vec_set
    global S_sen1_word
    global S_sen2_vec_set
    global S_sen2_word
    global u
    global U
    global NS_sen1_vec_set
    global NS_sen1_word
    global NS_sen2_word
    print("1")
    init(model, Sen1, Sen2)
    print("2")
    calc_simi_element(model, Sen1, Sen2, Sen1_word_vec_set, Sen2_word_vec_set)
    print("3")
    init_set()
    print("开始计算句子相似度")
    p = len(S_sen1_word)
    m = len(Sen1)

    print("开始计算分子")
    print(X)
    print(Y)
    print(S_sen1_word)
    # 分子
    tmp_list = [X[i]*Y[i] for i in range(len(S_sen1_word))]
    tmp_array = np.sum(np.array(tmp_list))
    print("开始计算分母左半部分")
    # 相似度函数的分母左半部分
    tmp = np.sqrt(np.sum(np.square(np.array(X[:m]))))
    print("开始计算分母右半部分")
    # 相似度函数的分母右半部分的左边
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
    print("句子相似度计算结束")
    return similarity