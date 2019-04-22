import sys
from SSFN_V4 import view

if __name__ == "__main__":
    app = view.QApplication(sys.argv)
    ex = view.MyFrame()
    """
    app.exec_()其实就是QApplication的方法，原来这个exec_()方法的作用
    是“进入程序的主循环直到exit()被调用”，如果没有这个方法，运行的时候窗口会闪退，
    所以show是有发挥作用的，但没有使用exec_()，所以没有进入程序的主循环就直接结束了。
    """
    # you are beautiful
    # you are a person
    sys.exit(app.exec_())