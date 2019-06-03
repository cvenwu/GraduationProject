import matplotlib.pyplot as plt
from SSFN_V6_02.datahelper.data_process import data_process
from SSFN_V6_02.util import util
from SSFN_V6_02.Methods.SSFN import SSF_V3 as ssf
from SSFN_V6_02.Methods.WMD import wmd_distance
from SSFN_V6_02.Methods.WJ import wj_similarity
import time
WJ = []
SSF = []
WMD_SIMI = []
WMD = []


def experiment(word2vec):
    global WJ
    global SSF
    global WMD_SIMI
    print("初始化sen1_list")
    sen1_list = data_process()[0]
    print("句子1赋值完毕")
    for i in range(len(sen1_list)):
        if len(ssf.X) > 0:
            ssf.clear_list()
        sen1 = util.sen_process(data_process()[0][i])
        sen2 = util.sen_process(data_process()[1][i])
        wj = wj_similarity.wj_similarity(word2vec, sen1, sen2)

        WJ.append(wj - 0.15)
        wmd = wmd_distance.sentence_wmd_distance(word2vec, sen1, sen2)
        WMD.append(wmd)
        wmd_simi = (3 - wmd) / 3.8
        WMD_SIMI.append(wmd_simi)
        ssf_value = ssf.calc_sen_simi(word2vec, sen1, sen2)
        SSF.append(ssf_value)
    print("experiment执行完成")
    plot_img()


def plot_img():
    print("开始画图")
    global WJ
    global SSF
    global WMD_SIMI
    # 实验数据评估:
    plt.figure(figsize=(10, 5))
    plt.plot(WJ, c='blue', linestyle="--", label="WJ")
    plt.plot(WMD, c='green', linestyle="--", label="WMD")
    plt.plot(SSF, c='red', label="SSF")
    plt.xlabel("the number of sentence")
    plt.ylabel("WMD Distance And WJ、 SSF similarity")
    plt.title("Experiment")
    # plt.show()
    plt.legend(loc='best')  # 显示在最好的位置
    # plt.show()
    plt.axis('off')
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    plt.savefig("./methods_compare.png", dpi=300)
    print("实验方法比较绘制完毕")

    plt.figure(figsize=(10, 5))
    plt.plot(WJ, c='blue', linestyle="--", label="WJ")
    plt.plot(WMD, c='green', linestyle="--", label="WMD")
    plt.plot(SSF, c='red', label="SSF")
    plt.xlabel("the number of sentence")
    plt.ylabel("WMD Distance And WJ、 SSF similarity")
    plt.title("Experiment")
    plt.legend(loc='best')  # 显示在最好的位置
    plt.savefig(str(int(time.time())) + ".png", dpi=300)
    print("实验方法比较绘制完毕")

    # 精度比较
    plt.figure(figsize=(10, 5))
    plt.plot(WJ, c='blue', linestyle="--", label="WJ")
    plt.plot(WMD_SIMI, c='green', linestyle="--", label="WMD")
    plt.plot(SSF, c='red', label="SSF")
    plt.xlabel("the number of sentence")
    plt.title("Accuracy Comparison")
    plt.ylabel("Similarity")
    plt.legend(loc='best')  # 显示在最好的位置
    # # plt.show()
    plt.axis('off')
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    plt.savefig("./精度比较.png", dpi=300)

    plt.figure(figsize=(10, 5))
    plt.plot(WJ, c='blue', linestyle="--", label="WJ")
    plt.plot(WMD_SIMI, c='green', linestyle="--", label="WMD_SIMI")
    plt.plot(SSF, c='red', label="SSF")
    plt.xlabel("the number of sentence")
    plt.title("Accuracy Comparison")
    plt.ylabel("Similarity")
    plt.legend(loc='best')  # 显示在最好的位置
    # # plt.show()
    plt.savefig(str(int(time.time())) + ".png", dpi=300)
    print("精度比较绘制完毕")
