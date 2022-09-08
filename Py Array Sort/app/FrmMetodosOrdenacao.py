# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmMetodosOrdenacao.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# Formulário responsável por mostrar informações sobre o métodos de ordenação
#

# Py Array Sort / app / FrmMetodosOrdenacao
# @author MRX
# Version : 1.0.0

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

        #Combobox itens
        self.cboMetodosOrdenacao.addItem("")
        self.cboMetodosOrdenacao.addItem("Sort[Python]")
        self.cboMetodosOrdenacao.addItem("Bubble Sort")
        self.cboMetodosOrdenacao.addItem("Shell Sort")

        self.cboMetodosOrdenacao.activated.connect(self.mostrarInfo)

    def retranslateUi(self, FrmMetodosOrdenacao):
        _translate = QtCore.QCoreApplication.translate
        FrmMetodosOrdenacao.setWindowTitle(_translate("FrmMetodosOrdenacao", "Sobre os Métodos de Ordenação de Vetores"))
        self.lblLoading.setText(_translate("FrmMetodosOrdenacao", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Métodos de Ordenação de Vetores</span></p></body></html>"))

    def mostrarInfo(self):
        if self.cboMetodosOrdenacao.currentText() == "Sort[Python]":
            self.txtMetodosOrdenacao.setPlainText("Sort - Python\n O método sort() permite que você organize uma lista "
                                                  "em ordem ascendente ou descendente. Ele recebe argumentos somente "
                                                  "nomeados: key e reverse. reverse determina se a lista é ordenada em "
                                                  "ordem ascendente ou descendente. key é uma função que gera um valor "
                                                  "intermediário para cada elemento. Esse valor é usado para fazer as "
                                                  "comparações durante o processo de ordenação.")

        elif self.cboMetodosOrdenacao.currentText() == "Bubble Sort":
            self.txtMetodosOrdenacao.setPlainText("Bubble Sort\n O bubble sort realiza múltiplas passagem por uma lista. "
                                                  "Ele compara itens adjacentes e troca aqueles que estão fora de ordem."
                                                  " Cada passagem pela lista coloca o próximo maior valor na sua posição"
                                                  " correta. Em essência, cada item se desloca como uma “bolha” para a"
                                                  " posição à qual pertence.")

        elif self.cboMetodosOrdenacao.currentText() == "Shell Sort":
            self.txtMetodosOrdenacao.setPlainText("Shell Sort\n O shell sort, às vezes chamado de “ordenação por "
                                                  "incrementos diminutos”, melhora a ordenação por inserção ao quebrar "
                                                  "a lista original em um número menor de sublistas, as quais são "
                                                  "ordenadas usando a ordenação por inserção. A forma única como essas"
                                                  " sublistas são escolhidas é a chave para o shell sort. Em vez de "
                                                  "quebrar a lista em sublistas de itens contíguos, o shell sort usa "
                                                  "um incremento i, às vezes chamado de gap, para criar uma sublista "
                                                  "escolhendo todos os itens que estão afastados i itens uns dos outros.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmMetodosOrdenacao = QtWidgets.QMainWindow()
    ui = Ui_FrmMetodosOrdenacao()
    ui.setupUi(FrmMetodosOrdenacao)

    FrmMetodosOrdenacao.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
    FrmMetodosOrdenacao.setFixedSize(597, 386)

    FrmMetodosOrdenacao.show()
    sys.exit(app.exec_())

