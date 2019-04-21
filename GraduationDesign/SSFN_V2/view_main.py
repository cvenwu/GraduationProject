import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QTextEdit, QLineEdit,
                             QGridLayout, QApplication, QPushButton)
from SSFN_V2 import SSF_V1 as ssf

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
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

        self.exitButton.clicked.connect(self.buttonClicked)
        self.calcButton.clicked.connect(self.buttonClicked)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('句子相似度计算')
        self.show()

    def calc_simi_sen(self):
        """
        通过获取组件中两个输入获取两个句子，调用ssf中的方法计算相似度
        相似度展现给simi组件
        :return: None
        """
        sen1 = self.sen1Edit.toPlainText().strip()
        sen2 = self.sen2Edit.toPlainText().strip()
        ssf.init(sen1, sen2)
        ssf.calc_simi_element(ssf.Sen1_word, ssf.Sen2_word, ssf.Sen1_word_vec_set, ssf.Sen2_word_vec_set)
        ssf.init_set()
        similarity = ssf.calc_sen_simi()
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
            sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())