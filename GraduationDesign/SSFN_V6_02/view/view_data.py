import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QTextEdit, QLineEdit, QMessageBox,
                             QGridLayout, QApplication, QPushButton)
from PyQt5.QtGui import QFont
from SSFN_V6_02.util.util import *
from SSFN_V6_02.Methods.SSFN import SSF_V3 as ssf
from SSFN_V6_02.Methods.WMD import wmd_distance
from SSFN_V6_02.Methods.WJ import wj_similarity
from SSFN_V6_02.experiment_show import result_img


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
        self.experButton = QPushButton("实验评估")
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
        grid.addWidget(self.experButton, 8, 0, 1, 2)

        # 控件添加事件
        self.exitButton.clicked.connect(self.buttonClicked)
        self.calcButton.clicked.connect(self.buttonClicked)
        self.initButton.clicked.connect(self.buttonClicked)
        self.experButton.clicked.connect(self.buttonClicked)

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

    def calc_result(self):
        """
        通过获取组件中两个输入获取两个句子，调用ssf中的方法计算相似度
        相似度展现给simi组件
        :return: None
        """
        if len(ssf.X) > 0:
            ssf.clear_list()

        if self.model is None:
            self.show_message_dialog("请先初始化模型")
            return
        sen1 = self.sen1Edit.toPlainText()
        sen2 = self.sen2Edit.toPlainText()
        if not is_legal_sent(sen1):
            self.show_message_dialog("句子1不可以为空")
            return
        if not is_legal_sent(sen2):
            self.show_message_dialog("句子2不可以为空")
            return
        sen1 = sen_process(sen1)
        sen2 = sen_process(sen2)
        print("句子1和2处理完毕")

        wj = wj_similarity.wj_similarity(self.model, sen1, sen2)
        self.wjSimiEdit.setText(str(wj))
        print("wj计算完成")
        wmd = wmd_distance.sentence_wmd_distance(self.model, sen1, sen2)
        self.wmdDistanceEdit.setText(str(wmd))
        print("wmd计算完成")
        ssf_value = ssf.calc_sen_simi(self.model, sen1, sen2)
        self.simiEdit.setText(str(ssf_value))
        print("SSF计算完成")

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
            self.calc_result()
        elif sender.text() == '初始化':
            # 加载模型
            print("开始加载模型。。。")
            self.model = load_model()
            print("加载完成。。。。。")
        elif sender.text() == '退出':
            sys.exit()
        elif sender.text() == '实验评估':
            result_img.experiment(self.model)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyFrame()
    sys.exit(app.exec_())
