import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QTextEdit, QLineEdit, QMessageBox,
                             QGridLayout, QApplication, QPushButton)
from PyQt5.QtGui import QFont
from SSFN_V6.util import *
from SSFN_V6 import SSF_V3 as ssf
from Test import Data_read
import matplotlib.pyplot as plt

class MyFrame(QWidget):
    model = None
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 调节字体大小
        QPushButton.setFont(self, QFont('SansSerif', 18))

        # 初始化控件
        self.initButton = QPushButton("初始化")
        self.calcButton = QPushButton("计算")
        self.exitButton = QPushButton('退出')
        self.sen1 = QLabel('句子1')
        self.sen2 = QLabel('句子2')
        self.simi = QLabel('相似度')
        self.wmdDistance = QLabel('WMD距离')
        self.wjSimi = QLabel('WJ')


        self.sen1Edit = QTextEdit()
        self.sen2Edit = QTextEdit()
        self.simiEdit = QLineEdit()
        self.wmdDistanceEdit = QLineEdit()
        self.wjSimiEdit = QLineEdit()
        self.simiEdit.setEnabled(False)
        self.wmdDistanceEdit.setEnabled(False)
        self.wjSimiEdit.setEnabled(False)


        # 我们创建了一个有三个标签的窗口。两个行编辑和一个文版编辑，这是用QGridLayout模块搞定的。
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.sen1, 1, 0)
        grid.addWidget(self.sen1Edit, 1, 1)

        grid.addWidget(self.sen2, 2, 0)
        grid.addWidget(self.sen2Edit, 2, 1)

        grid.addWidget(self.simi, 3, 0)
        # 创建标签之间的空间。
        # 我们可以指定组件的跨行和跨列的大小。这里我们指定这个元素跨5行显示
        # grid.addWidget(self.simiEdit, 3, 1, 5, 1)
        grid.addWidget(self.simiEdit, 3, 1)
        grid.addWidget(self.wmdDistance, 4, 0)
        grid.addWidget(self.wmdDistanceEdit, 4, 1)
        grid.addWidget(self.wjSimi, 5, 0)
        grid.addWidget(self.wjSimiEdit, 5, 1)
        # 我们可以init按钮在第4行第0列开始显示，这个元素占据1行，并且跨2列
        grid.addWidget(self.initButton, 6, 0, 1, 2)
        grid.addWidget(self.exitButton, 7, 0)
        grid.addWidget(self.calcButton, 7, 1)

        # 控件添加事件
        self.exitButton.clicked.connect(self.buttonClicked)
        self.calcButton.clicked.connect(self.buttonClicked)
        self.initButton.clicked.connect(self.buttonClicked)
        self.setLayout(grid)
        self.setGeometry(550, 290, 820, 500)
        self.setWindowTitle('句子相似度计算')
        self.show()

    def show_message_dialog(self, message):
        """
        定义一个方法用来展示对话框
        :param message: 对话框上的消息
        :return: None
        """
        self.message = QMessageBox.question(self, '消息', message,
                                         QMessageBox.Yes, QMessageBox.No)

    def show_result(self):
        """
        通过获取组件中两个输入获取两个句子，调用ssf中的方法计算相似度
        相似度展现给simi组件
        :return: None
        """
        print(type(self.model))
        print(self.model)
        if self.model is None:
            self.show_message_dialog("请先初始化模型")
            return
        sen1 = self.sen1Edit.toPlainText().strip()
        sen2 = self.sen2Edit.toPlainText().strip()
        if sen1 == '':
            self.show_message_dialog("句子1不可以为空")
            return
        if sen2 == '':
            self.show_message_dialog("句子2不可以为空")
            return

        # 如果之前计算过，需要将之前所有计算过的列表全部清空
        if len(ssf.X) > 0:
            ssf.Sen1_word.clear()
            ssf.Sen2_word.clear()
            ssf.Sen1_word_vec_set.clear()
            ssf.Sen2_word_vec_set.clear()
            ssf.S_sen1_vec_set.clear()
            ssf.NS_sen1_vec_set.clear()
            ssf.S_sen2_vec_set.clear()
            ssf.S_sen1_word.clear()
            ssf.NS_sen1_word.clear()
            ssf.S_sen2_word.clear()
            ssf.NS_sen2_word.clear()
            ssf.u.clear()
            ssf.U.clear()
            ssf.X.clear()
            ssf.Y.clear()
            ssf.maxsim = 0

        WJ = []
        SSF = []
        WMD = []
        WMD_SIMI = []
        Data_read.compute()
        for i in range(250):
            print("处理句子1")
            sen1 = sen_process(Data_read.sen1_list[i])
            print("句子1处理完毕")
            print("处理句子2")
            sen2 = sen_process(Data_read.sen2_list[i])
            print("句子2处理完毕")
            print("计算WJ：")
            wj = self.model.sentence_similarity(sen1, sen2)
            WJ.append(wj-0.15)
            # @ TODO: 这里暂时使用没有涉及权重的计算句子相似度，明天问下老师WJ算法的权重怎么算
            self.wjSimiEdit.setText(str(wj))

            print("计算WMD：")
            wmd = self.model.sentence_wmd_distance(sen1, sen2)
            wmd_simi = (3 - wmd) / 3.0
            WMD_SIMI.append(wmd_simi)
            self.wmdDistanceEdit.setText(str(wmd))
            WMD.append(wmd)
            print(wmd)
            print("计算SSF:")
            ssf_value = ssf.calc_sen_simi(self.model, sen1, sen2)
            self.simiEdit.setText(str(ssf_value))
            SSF.append(ssf_value)

            if len(ssf.X) > 0:
                ssf.Sen1_word.clear()
                ssf.Sen2_word.clear()
                ssf.Sen1_word_vec_set.clear()
                ssf.Sen2_word_vec_set.clear()
                ssf.S_sen1_vec_set.clear()
                ssf.NS_sen1_vec_set.clear()
                ssf.S_sen2_vec_set.clear()
                ssf.S_sen1_word.clear()
                ssf.NS_sen1_word.clear()
                ssf.S_sen2_word.clear()
                ssf.NS_sen2_word.clear()
                ssf.u.clear()
                ssf.U.clear()
                ssf.X.clear()
                ssf.Y.clear()
                ssf.maxsim = 0

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
        plt.savefig("methods_compare.png", dpi=100)

        # 精度比较
        # plt.figure(figsize=(10, 5))
        # plt.plot(WJ, c='blue', linestyle="--", label="WJ")
        # plt.plot(WMD_SIMI, c='green', linestyle="--", label="WMD")
        # plt.plot(SSF, c='red', label="SSF")
        # plt.xlabel("the number of sentence")
        # plt.title("Accuracy Comparison")
        # plt.ylabel("Similarity")
        # plt.legend(loc='best')  # 显示在最好的位置
        # # # plt.show()
        # plt.axis('off')
        # plt.gca().xaxis.set_major_locator(plt.NullLocator())
        # plt.gca().yaxis.set_major_locator(plt.NullLocator())
        # plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
        # plt.margins(0, 0)
        # plt.savefig("精度比较.png", dpi=300)

    # 这个例子里有俩按钮，buttonClicked()方法决定了是哪个按钮能调用sender()方法。
    # 两个按钮都和同一个slot绑定。
    # 我们用调用sender()方法的方式决定了事件源。状态栏显示了被点击的按钮。
    def buttonClicked(self):
        """
        按钮点击事件，根据按钮上的文本来区分不同功能
            计算：计算句子相似度
            退出：直接退出
        :return: None
        """
        sender = self.sender()
        if sender.text() == '计算':
            print("1")
            self.show_result()
            print("2")
        elif sender.text() == '初始化':
            # 加载模型
            print("开始加载模型。。。")
            self.model = load_model()
            print("加载完成。。。。。")
        elif sender.text() == '退出':
            sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyFrame()
    sys.exit(app.exec_())
