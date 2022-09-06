# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmMetodosOrdenacao.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FrmMetodosOrdenacao(object):
    def setupUi(self, FrmMetodosOrdenacao):
        FrmMetodosOrdenacao.setObjectName("FrmMetodosOrdenacao")
        FrmMetodosOrdenacao.resize(597, 386)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrmMetodosOrdenacao.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(FrmMetodosOrdenacao)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 601, 391))
        self.frame.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cboMetodosOrdenacao = QtWidgets.QComboBox(self.frame)
        self.cboMetodosOrdenacao.setGeometry(QtCore.QRect(170, 60, 271, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cboMetodosOrdenacao.setFont(font)
        self.cboMetodosOrdenacao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cboMetodosOrdenacao.setCurrentText("")
        self.cboMetodosOrdenacao.setObjectName("cboMetodosOrdenacao")
        self.lblLoading = QtWidgets.QLabel(self.frame)
        self.lblLoading.setGeometry(QtCore.QRect(170, 40, 201, 16))
        self.lblLoading.setObjectName("lblLoading")
        self.txtMetodosOrdenacao = QtWidgets.QTextEdit(self.frame)
        self.txtMetodosOrdenacao.setGeometry(QtCore.QRect(120, 120, 361, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtMetodosOrdenacao.setFont(font)
        self.txtMetodosOrdenacao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtMetodosOrdenacao.setReadOnly(True)
        self.txtMetodosOrdenacao.setObjectName("txtMetodosOrdenacao")
        FrmMetodosOrdenacao.setCentralWidget(self.centralwidget)

        self.retranslateUi(FrmMetodosOrdenacao)
        QtCore.QMetaObject.connectSlotsByName(FrmMetodosOrdenacao)

    def retranslateUi(self, FrmMetodosOrdenacao):
        _translate = QtCore.QCoreApplication.translate
        FrmMetodosOrdenacao.setWindowTitle(_translate("FrmMetodosOrdenacao", "Sobre os Métodos de Ordenação de Vetores"))
        self.lblLoading.setText(_translate("FrmMetodosOrdenacao", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Métodos de Ordenação de Vetores</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmMetodosOrdenacao = QtWidgets.QMainWindow()
    ui = Ui_FrmMetodosOrdenacao()
    ui.setupUi(FrmMetodosOrdenacao)
    FrmMetodosOrdenacao.show()
    sys.exit(app.exec_())

