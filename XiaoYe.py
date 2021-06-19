# -*- coding: utf-8 -*-
import ctypes  # 需要用到的库
import sys
from xiaoye_UI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from craw import craw


class Ui_Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Ui_Main, self).__init__(parent=None)
        self.setWindowIcon(QIcon('house.png'))
        self.setupUi(self)
        self.label.setPixmap(QPixmap('city.png'))
        self.pushButton.clicked.connect(self.onclick_button)
        self.pushButton_2.clicked.connect(self.onclick_button2)

    def onclick_button(self):
        name = self.lineEdit.text()
        if name == '合肥':
            craw(name='hf')
        else:
            craw()
        msg_box = QMessageBox(QMessageBox.Information, '提示', '房源爬取完成！')
        msg_box.exec_()

    def onclick_button2(self):
        name = self.lineEdit.text()
        if name == '合肥':
            QtGui.QDesktopServices.openUrl(QtCore.QUrl('http://localhost:63342/python_finalwork/index_hf.html?_ijt=jc6pvcdr3nudd977qfq3h1bmbt'))
        else:
            QtGui.QDesktopServices.openUrl(QtCore.QUrl('http://localhost:63342/python_finalwork/index.html?_ijt=scor7v2s64cdl1bprj7k7nf65u'))


if __name__ == '__main__':
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
    app = QApplication(sys.argv)
    window = Ui_Main()
    window.show()
    sys.exit(app.exec_())
