import pandas as pd
from SSFN_V6_02.util import util


def data_process(num=250):
    """
    从数据集中获取实验评估数据，默认为250条，将数据加载到句子1和2对应的列表中并进行返回
    :param num: 实验数据的条数，默认为250
    :return: 句子1组成的集合，句子2组成的集合
    """
    content = pd.read_csv(util.data_path(), sep='\n', header=None)
    content = content.head(num)

    sen1_list = []
    sen2_list = []
    print("开始处理实验数据")
    for i in range(num):
        content_split = content[0][i].split('\t')
        sen1_list.append(content_split[5])
        sen2_list.append(content_split[6])
    print("实验数据处理完成")
    return sen1_list, sen2_list
