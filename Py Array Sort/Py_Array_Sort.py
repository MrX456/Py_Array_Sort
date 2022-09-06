# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Py_Array_Sort.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FrmSplash(object):
    def setupUi(self, FrmSplash):
        FrmSplash.setObjectName("FrmSplash")
        FrmSplash.resize(462, 237)
        FrmSplash.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrmSplash.setWindowIcon(icon)
        FrmSplash.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(FrmSplash)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(80, 200, 321, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.picIcon = QtWidgets.QLabel(self.centralwidget)
        self.picIcon.setGeometry(QtCore.QRect(190, 50, 71, 81))
        self.picIcon.setText("")
        self.picIcon.setPixmap(QtGui.QPixmap("resources/icon_small.png"))
        self.picIcon.setObjectName("picIcon")
        self.lblLoading = QtWidgets.QLabel(self.centralwidget)
        self.lblLoading.setGeometry(QtCore.QRect(190, 150, 81, 16))
        self.lblLoading.setObjectName("lblLoading")
        FrmSplash.setCentralWidget(self.centralwidget)

        self.retranslateUi(FrmSplash)
        QtCore.QMetaObject.connectSlotsByName(FrmSplash)

    def retranslateUi(self, FrmSplash):
        _translate = QtCore.QCoreApplication.translate
        FrmSplash.setWindowTitle(_translate("FrmSplash", "Loading"))
        self.lblLoading.setText(_translate("FrmSplash", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Carregando...</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmSplash = QtWidgets.QMainWindow()
    ui = Ui_FrmSplash()
    ui.setupUi(FrmSplash)
    FrmSplash.show()
    sys.exit(app.exec_())

