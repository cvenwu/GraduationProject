import sys
from SSFN_V6_02.view import view_data

if __name__ == "__main__":
    app = view_data.QApplication(sys.argv)
    ex = view_data.MyFrame()
    sys.exit(app.exec_())
