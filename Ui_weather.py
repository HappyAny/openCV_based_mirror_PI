# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\weather\weather.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import fun
import json
fun.main()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView.setGeometry(QtCore.QRect(70, 40, 221, 191))
        self.graphicsView.setObjectName("graphicsView")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(340, 40, 391, 192))
        def test():
            a=''
            with open("news.json", 'r') as f:
                tmp=json.load(f)
            print(tmp[0][0])
            for x in tmp:
                for y in x:
                    a += y+'\n'
            return a
        self.textBrowser.setText(test())
        self.textBrowser.setObjectName("textBrowser")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(40, 290, 101, 101))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(40, 410, 101, 51))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(160, 290, 101, 101))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(160, 410, 101, 51))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView_4.setGeometry(QtCore.QRect(280, 290, 101, 101))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(280, 410, 101, 51))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView_5.setGeometry(QtCore.QRect(400, 290, 101, 101))
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(400, 410, 101, 51))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.graphicsView_6 = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView_6.setGeometry(QtCore.QRect(520, 290, 101, 101))
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(520, 410, 101, 51))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.graphicsView_7 = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView_7.setGeometry(QtCore.QRect(640, 290, 101, 101))
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_7.setGeometry(QtCore.QRect(640, 410, 101, 51))
        self.textBrowser_7.setObjectName("textBrowser_7")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

