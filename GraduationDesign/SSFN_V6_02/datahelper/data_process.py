import pandas as pd
from SSFN_V6_02.util import util


def data_process(num=250):
    """
    从数据集中获取实验评估数据，默认为250条，将数据加载到句子1和2对应的列表中并进行返回
    :param num: 实验数据的条数，默认为250
    :return: None
    """
    content = pd.read_csv(util.data_path(), sep='\n', header=None)
    content = content.head(num)

    sen1_list = []
    sen2_list = []
    for i in range(num):
        print(content[0][i].split('\t')[5])
        print(content[0][i].split('\t')[6])
        content_split = content[0][i].split('\t')
        sen1_list.append(content_split[5])
        sen2_list.append(content_split[6])
    print(len(sen1_list))  # 250
    print(len(sen2_list))  # 250
    return sen1_list, sen2_list
