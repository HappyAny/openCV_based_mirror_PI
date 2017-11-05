# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\weather\news.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import fun
import json
import random
import socket
fun.main()

global data

def recive():
    server_addr = '10.1.0.173'
    server_port = 28888

    sk = socket.socket()
    sk.bind((server_addr, server_port))
    sk.listen(1)
    conn, addr = sk.accept()
    data = conn.recv(128)
    if data == b'1':
        print('上')
    elif data == b'2':
        print('下')
    elif data == b'3':
        print('左')
    elif data == b'4':
        print('右')
    data = str(data)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        def outputWeb():
            a=''
            with open("news.json",'r')as f:
                tmp=json.load(f)
            for x in tmp[0]:
                a+=x+'\n'
                return a
        def outPutNews():
            b=''
            with open("news.json",'r')as f:
                tmp=json.load(f)
                i=1
                j=1
                return tmp[i][j]
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(310, 80, 151, 71))
        self.textBrowser.setObjectName("textBrowser")
        # self.textBrowser.setText(outputWeb())
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(190, 170, 391, 71))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_2.setText(outPutNews())
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(190, 260, 391, 71))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(190, 350, 391, 71))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(190, 440, 391, 71))
        self.textBrowser_5.setObjectName("textBrowser_5")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # for x,y=0 in tmp:
        #     def outputWeb(n):
        #         a=''
        #         with open("news.json",'r')as f:
        #             tmp=json.load(f)
        #             for x in tmp[0]:
        #                  a+=x+'\n'
        #                  return a

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

        items = [0, 1, 2]
        random.shuffle(items)
        # i=0
        # def outputWeb():
        #     a = ''
        #     with open("news.json", 'r')as f:
        #         tmp = json.load(f)
        #         for x in tmp[items[i]]:
        #             a += x + '\n'
        #             i += 1
        #         return a
        # def outputNews()
        #     a=''
        #     with open("news.json",'r')as f:
        #         tmp=json.load(f)
        #         for x in tmp[items[i][0]]
        #
        #     self.textBrowser.setText(outputWeb())
        # a=[items][i]
        with open("news.json",'r')as f:
            tmp=json.load(f)
            n=0
            m=0
            self.textBrowser.setText(tmp[int(items[n])][m])
            m = m + 1
            self.textBrowser_2.setText(tmp[int(items[n])][m])
            m = m + 1
            self.textBrowser_3.setText(tmp[int(items[n])][m])
            m = m + 1
            self.textBrowser_4.setText(tmp[int(items[n])][m])
            m = m + 1
            self.textBrowser_5.setText(tmp[int(items[n])][m])
            m = m + 1
            x=data
            if(x==1):
                # self.textBrowser.setText(tmp [int(items[n])][m])
                # m=m+1
                self.textBrowser_2.setText(tmp [int(items[n])][m])
                m = m + 1
                self.textBrowser_3.setText(tmp [int(items[n])][m])
                m = m + 1
                self.textBrowser_4.setText(tmp [int(items[n])][m])
                m = m + 1
                self.textBrowser_5.setText(tmp [int(items[n])][m])
                m=m+1
            n=n+1
            if(x==3):
                m=0
                self.textBrowser.setText(tmp[int(items[n])][m])
                m = m + 1
                self.textBrowser_2.setText(tmp[int(items[n])][m])
                m = m + 1
                self.textBrowser_3.setText(tmp[int(items[n])][m])
                m = m + 1
                self.textBrowser_4.setText(tmp[int(items[n])][m])
                m = m + 1
                self.textBrowser_5.setText(tmp[int(items[n])][m])
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

