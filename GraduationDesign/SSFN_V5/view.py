import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QTextEdit, QLineEdit, QMessageBox,
                             QGridLayout, QApplication, QPushButton)
from PyQt5.QtGui import QFont
from SSFN_V5 import SSF_V2 as ssf


class MyFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 调节字体大小
        QPushButton.setFont(self, QFont('SansSerif', 18))

        # 初始化控件
        self.calcButton = QPushButton("计算")
        self.exitButton = QPushButton('退出')
        self.sen1 = QLabel('句子1')
        self.sen2 = QLabel('句子2')
        self.simi = QLabel('相似度')

        self.sen1Edit = QTextEdit()
        self.sen2Edit = QTextEdit()
        self.simiEdit = QLineEdit()
        self.simiEdit.setEnabled(False)

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
        grid.addWidget(self.exitButton)
        grid.addWidget(self.calcButton)

        # 控件添加事件
        self.exitButton.clicked.connect(self.buttonClicked)
        self.calcButton.clicked.connect(self.buttonClicked)

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

    def calc_simi_sen(self):
        """
        通过获取组件中两个输入获取两个句子，调用ssf中的方法计算相似度
        相似度展现给simi组件
        :return: None
        """
        sen1 = self.sen1Edit.toPlainText().strip()
        sen2 = self.sen2Edit.toPlainText().strip()
        if sen1 == '':
            self.show_message_dialog("句子1不可以为空")
            return
        if sen2 == '':
            self.show_message_dialog("句子2不可以为空")
            return
        print(sen1)
        print(sen2)

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

        ssf.init(sen1, sen2)
        ssf.calc_simi_element(ssf.Sen1_word, ssf.Sen2_word, ssf.Sen1_word_vec_set, ssf.Sen2_word_vec_set)
        ssf.init_set()
        similarity = ssf.calc_sen_simi()
        print(ssf.u)
        print(ssf.S_sen1_word)
        print(ssf.X)
        print(ssf.Y)
        self.simiEdit.setText(str(similarity))

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
            self.calc_simi_sen()
        elif sender.text() == '退出':
            sys.exit()

