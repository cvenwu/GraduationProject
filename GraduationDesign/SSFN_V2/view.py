"""
组件能跨列和跨行展示，这个例子里，我们就试试这个功能。

"""

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication, QPushButton)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        calcButton = QPushButton("计算")
        exitButton = QPushButton('退出')

        title = QLabel('句子1')
        author = QLabel('句子2')
        review = QLabel('相似度')

        titleEdit = QTextEdit()
        authorEdit = QTextEdit()
        reviewEdit = QTextEdit()
        reviewEdit.setEnabled(False)

        # 我们创建了一个有三个标签的窗口。两个行编辑和一个文版编辑，这是用QGridLayout模块搞定的。
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        # 创建标签之间的空间。
        # 我们可以指定组件的跨行和跨列的大小。这里我们指定这个元素跨5行显示
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        grid.addWidget(exitButton)
        grid.addWidget(calcButton)

        exitButton.clicked.connect(self.buttonClicked)
        calcButton.clicked.connect(self.buttonClicked)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()

    # 这个例子里有俩按钮，buttonClicked()方法决定了是哪个按钮能调用sender()方法。
    # 两个按钮都和同一个slot绑定。
    # 我们用调用sender()方法的方式决定了事件源。状态栏显示了被点击的按钮。
    def buttonClicked(self):
        # sender = self.sender()
        # self.statusBar().showMessage(sender.text() + ' was pressed')
        # print(sender.text())
        # sys.exit(app.exec_())
        sender = self.sender()
        if sender.text() == '计算':
            pass
        elif sender.text() == '退出':
            sys.exit(app.exec_())



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())