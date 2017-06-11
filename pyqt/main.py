import sys
from PyQt5 import QtWidgets, QtGui


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    b = QtWidgets.QLabel(w)
    b.setPixmap(QtGui.QPixmap("wtm3.png"))
    w.setWindowTitle('PyQt')
    w.setCentralWidget(b)
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
