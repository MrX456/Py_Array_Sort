# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmHome.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# Formulário principal, responsável pela ordenação dos arrays
#

# Py Array Sort / app / FrmHome
# @author MRX
# Version : 1.0.0

from PyQt5 import QtCore, QtGui, QtWidgets
from app.FrmSobre import Ui_FrmSobre
from app.FrmMetodosOrdenacao import Ui_FrmMetodosOrdenacao
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QFont
from sort.BubbleSort import Bubblesort
from sort.ShellSort import Shellsort

class Ui_FrmHome(object):

    array = []

    def setupUi(self, FrmHome):
        FrmHome.setObjectName("FrmHome")
        FrmHome.resize(1000, 553)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrmHome.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(FrmHome)
        self.centralwidget.setObjectName("centralwidget")
        self.frameBackground = QtWidgets.QFrame(self.centralwidget)
        self.frameBackground.setGeometry(QtCore.QRect(0, 0, 1001, 581))
        self.frameBackground.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.frameBackground.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBackground.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBackground.setObjectName("frameBackground")
        self.frameElementos = QtWidgets.QFrame(self.frameBackground)
        self.frameElementos.setGeometry(QtCore.QRect(280, 131, 451, 261))
        self.frameElementos.setFrameShape(QtWidgets.QFrame.Box)
        self.frameElementos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameElementos.setLineWidth(3)
        self.frameElementos.setObjectName("frameElementos")
        self.btnAdd = QtWidgets.QPushButton(self.frameElementos)
        self.btnAdd.setGeometry(QtCore.QRect(320, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnAdd.setFont(font)
        self.btnAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAdd.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 255);")
        self.btnAdd.setObjectName("btnAdd")
        self.lblNumero = QtWidgets.QLabel(self.frameElementos)
        self.lblNumero.setGeometry(QtCore.QRect(60, 50, 71, 20))
        self.lblNumero.setObjectName("lblNumero")
        self.txtNumero = QtWidgets.QLineEdit(self.frameElementos)
        self.txtNumero.setGeometry(QtCore.QRect(140, 40, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtNumero.setFont(font)
        self.txtNumero.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtNumero.setMaxLength(2)
        self.txtNumero.setObjectName("txtNumero")
        self.lblMetodosOrdenacao = QtWidgets.QLabel(self.frameElementos)
        self.lblMetodosOrdenacao.setGeometry(QtCore.QRect(60, 150, 71, 20))
        self.lblMetodosOrdenacao.setObjectName("lblMetodosOrdenacao")
        self.cboMetodosOrdenacao = QtWidgets.QComboBox(self.frameElementos)
        self.cboMetodosOrdenacao.setEnabled(False)
        self.cboMetodosOrdenacao.setGeometry(QtCore.QRect(140, 140, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cboMetodosOrdenacao.setFont(font)
        self.cboMetodosOrdenacao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cboMetodosOrdenacao.setCurrentText("")
        self.cboMetodosOrdenacao.setObjectName("cboMetodosOrdenacao")
        self.btnOrdenar = QtWidgets.QPushButton(self.frameElementos)
        self.btnOrdenar.setEnabled(False)
        self.btnOrdenar.setGeometry(QtCore.QRect(130, 200, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnOrdenar.setFont(font)
        self.btnOrdenar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnOrdenar.setStyleSheet("background-color: rgb(180, 180, 180);\n"
"color: rgb(0, 170, 255);")
        self.btnOrdenar.setObjectName("btnOrdenar")
        self.btnLimpar = QtWidgets.QPushButton(self.frameElementos)
        self.btnLimpar.setGeometry(QtCore.QRect(250, 200, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnLimpar.setFont(font)
        self.btnLimpar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLimpar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 255);")
        self.btnLimpar.setObjectName("btnLimpar")
        self.btnPronto = QtWidgets.QPushButton(self.frameElementos)
        self.btnPronto.setGeometry(QtCore.QRect(180, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnPronto.setFont(font)
        self.btnPronto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPronto.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 255);")
        self.btnPronto.setObjectName("btnPronto")
        self.frameArray = QtWidgets.QFrame(self.frameBackground)
        self.frameArray.setGeometry(QtCore.QRect(280, 60, 451, 61))
        self.frameArray.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.frameArray.setFrameShape(QtWidgets.QFrame.Box)
        self.frameArray.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameArray.setLineWidth(3)
        self.frameArray.setObjectName("frameArray")
        self.lblArray = QtWidgets.QLabel(self.frameArray)
        self.lblArray.setGeometry(QtCore.QRect(10, 10, 51, 20))
        self.lblArray.setObjectName("lblArray")
        self.lblArrayElements = QtWidgets.QLabel(self.frameArray)
        self.lblArrayElements.setGeometry(QtCore.QRect(10, 30, 431, 20))
        self.lblArrayElements.setObjectName("lblArrayElements")
        self.frameArrayOrdenado = QtWidgets.QFrame(self.frameBackground)
        self.frameArrayOrdenado.setGeometry(QtCore.QRect(280, 411, 451, 61))
        self.frameArrayOrdenado.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(0, 85, 255);")
        self.frameArrayOrdenado.setFrameShape(QtWidgets.QFrame.Box)
        self.frameArrayOrdenado.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameArrayOrdenado.setLineWidth(3)
        self.frameArrayOrdenado.setObjectName("frameArrayOrdenado")
        self.lblArrayOrdenado = QtWidgets.QLabel(self.frameArrayOrdenado)
        self.lblArrayOrdenado.setGeometry(QtCore.QRect(10, 10, 321, 20))
        self.lblArrayOrdenado.setObjectName("lblArrayOrdenado")
        self.lblArrayElementsOrdenado = QtWidgets.QLabel(self.frameArrayOrdenado)
        self.lblArrayElementsOrdenado.setGeometry(QtCore.QRect(10, 30, 431, 20))
        self.lblArrayElementsOrdenado.setObjectName("lblArrayElementsOrdenado")
        FrmHome.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FrmHome)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        self.menuAjud = QtWidgets.QMenu(self.menubar)
        self.menuAjud.setObjectName("menuAjud")
        self.menuOp_es = QtWidgets.QMenu(self.menubar)
        self.menuOp_es.setObjectName("menuOp_es")
        FrmHome.setMenuBar(self.menubar)
        self.actionSair = QtWidgets.QAction(FrmHome)
        self.actionSair.setObjectName("actionSair")
        self.actionM_todos_de_Ordena_o = QtWidgets.QAction(FrmHome)
        self.actionM_todos_de_Ordena_o.setObjectName("actionM_todos_de_Ordena_o")
        self.actionSobre = QtWidgets.QAction(FrmHome)
        self.actionSobre.setObjectName("actionSobre")
        self.actionManual = QtWidgets.QAction(FrmHome)
        self.actionManual.setObjectName("actionManual")
        self.menuAjud.addSeparator()
        self.menuAjud.addAction(self.actionM_todos_de_Ordena_o)
        self.menuAjud.addAction(self.actionSobre)
        self.menuAjud.addAction(self.actionManual)
        self.menuOp_es.addAction(self.actionSair)
        self.menubar.addAction(self.menuAjud.menuAction())
        self.menubar.addAction(self.menuOp_es.menuAction())

        self.retranslateUi(FrmHome)
        QtCore.QMetaObject.connectSlotsByName(FrmHome)

        self.lblArrayElements.setText("")
        self.lblArrayElementsOrdenado.setText("")

        #Menu principal
        self.actionM_todos_de_Ordena_o.triggered.connect(self.abrirMetodosOrdenacao)
        self.actionSobre.triggered.connect(self.abrirSobre)
        #abrir manual******************************************************************************************mude cor do botao ao destivar
        self.actionSair.triggered.connect(self.sair)

        #Combobox itens
        #self.cboMetodosOrdenacao.setEnabled(True)
        self.cboMetodosOrdenacao.addItem("Sort[Python]")
        self.cboMetodosOrdenacao.addItem("Bubble Sort")
        self.cboMetodosOrdenacao.addItem("Shell Sort")
        self.cboMetodosOrdenacao.addItem("Não Está Ordenado")

        self.btnAdd.clicked.connect(self.addItemToArray)
        self.btnPronto.clicked.connect(self.fecharArray)
        self.btnOrdenar.clicked.connect(self.ordenarArray)
        self.btnLimpar.clicked.connect(self.setDefaultState)

        self.txtNumero.textChanged.connect(self.isNumber)

    def retranslateUi(self, FrmHome):
        _translate = QtCore.QCoreApplication.translate
        FrmHome.setWindowTitle(_translate("FrmHome", "Py Array Sort 1.0.0"))
        self.btnAdd.setToolTip(_translate("FrmHome", "Adicionar valor no array"))
        self.btnAdd.setText(_translate("FrmHome", "Adicionar"))
        self.lblNumero.setText(_translate("FrmHome", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Número :</span></p></body></html>"))
        self.lblMetodosOrdenacao.setText(_translate("FrmHome", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Método :</span></p></body></html>"))
        self.btnOrdenar.setText(_translate("FrmHome", "Ordenar"))
        self.btnLimpar.setToolTip(_translate("FrmHome", "Limpar array"))
        self.btnLimpar.setText(_translate("FrmHome", "Limpar"))
        self.btnPronto.setToolTip(_translate("FrmHome", "Finalizar array"))
        self.btnPronto.setText(_translate("FrmHome", "Pronto"))
        self.lblArray.setText(_translate("FrmHome", "<html><head/><body><p><span style=\" font-size:12pt; color:#000000;\">Array :</span></p></body></html>"))
        self.lblArrayElements.setText(_translate("FrmHome", "<html><head/><body><p><br/></p></body></html>"))
        self.lblArrayOrdenado.setText(_translate("FrmHome", "<html><head/><body><p><span style=\" font-size:12pt; color:#0055ff;\">Array Ordenado :</span></p></body></html>"))
        self.lblArrayElementsOrdenado.setText(_translate("FrmHome", "<html><head/><body><p><br/></p></body></html>"))
        self.menuAjud.setTitle(_translate("FrmHome", "Ajuda"))
        self.menuOp_es.setTitle(_translate("FrmHome", "Opções"))
        self.actionSair.setText(_translate("FrmHome", "Sair"))
        self.actionM_todos_de_Ordena_o.setText(_translate("FrmHome", "Métodos de Ordenação"))
        self.actionSobre.setText(_translate("FrmHome", "Sobre"))
        self.actionManual.setText(_translate("FrmHome", "Manual"))

    #Region - Menu principal

    def abrirMetodosOrdenacao(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FrmMetodosOrdenacao()
        self.ui.setupUi(self.window)
        self.window.show()

    def abrirSobre(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_FrmSobre()
        self.ui.setupUi(self.window)
        self.window.show()

    def sair(self):
        msg = QMessageBox()
        msg.setStyleSheet("background-color: rgb(0, 170, 255);")
        msg.setWindowTitle("Sair?")
        msg.setText("Deseja sair do Py Array Sort?")
        msg.setIcon(QMessageBox.Question)

        btnOptionA = msg.addButton("Sim", QMessageBox.YesRole)
        btnOptionB = msg.addButton("Não", QMessageBox.NoRole)

        msg.exec_()

        if msg.clickedButton() == btnOptionA:
            sys.exit(0)

    #Endregion

    def addItemToArray(self):
         if self.txtNumero.text() != "":

            if len(self.array) < 3: #tamanho máximo 10 itens

                self.array.append(self.txtNumero.text())

                self.lblArrayElements.setFont(QFont('Arial', 12,))
                self.lblArrayElements.setStyleSheet("font-weight: bold")

                if(self.lblArrayElements.text() == ""):
                    self.lblArrayElements.setText(self.txtNumero.text())
                else:
                    self.lblArrayElements.setText(self.lblArrayElements.text() + ", " + self.txtNumero.text())

            else:
                msg = QMessageBox()
                msg.setStyleSheet("background-color: rgb(0, 170, 255);")
                msg.setWindowTitle("Mensagem")
                msg.setText("Impossivel adicionar elemento! O array não pode ter mais de 10 elementos!")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()

            self.txtNumero.setText("")
            self.txtNumero.setFocus()

    def fecharArray(self):
        if len(self.array) > 0:
            self.txtNumero.setEnabled(False)
            self.txtNumero.setText("")
            self.btnAdd.setEnabled(False)
            self.btnAdd.setStyleSheet("background-color: rgb(180, 180, 180);\n""color: rgb(0, 170, 255);")
            self.btnPronto.setEnabled(False)
            self.btnPronto.setStyleSheet("background-color: rgb(180, 180, 180);\n""color: rgb(0, 170, 255);")
            self.cboMetodosOrdenacao.setEnabled(True)
            self.btnOrdenar.setEnabled(True)
            self.btnOrdenar.setStyleSheet("background-color: rgb(255, 255, 255);\n""color: rgb(0, 170, 255);")
        else:
             msg = QMessageBox()
             msg.setStyleSheet("background-color: rgb(0, 170, 255);")
             msg.setWindowTitle("Mensagem")
             msg.setText("Não existem elementos no array!")
             msg.setIcon(QMessageBox.Information)
             msg.exec_()

    def ordenarArray(self):

        self.lblArrayElementsOrdenado.setText("")

        auxArray = list(self.array) #copiar array original para auxiliar para manter original inalterado

        print("Array original")
        print(auxArray)

        if self.cboMetodosOrdenacao.currentText() == "Sort[Python]":
            auxArray.sort() #ordenar array auxliar
            print(self.cboMetodosOrdenacao.currentText())
            print(auxArray)

        elif self.cboMetodosOrdenacao.currentText() == "Bubble Sort":
            bubblesort = Bubblesort()
            bubblesort.sort(auxArray)
            print(self.cboMetodosOrdenacao.currentText())
            print(auxArray)

        elif self.cboMetodosOrdenacao.currentText() == "Shell Sort":
            shellsort = Shellsort()
            print(self.cboMetodosOrdenacao.currentText())
            shellsort.sort(auxArray)
            print(auxArray)

        elif self.cboMetodosOrdenacao.currentText() == "Não Está Ordenado":
            pass

        self.lblArrayOrdenado.setFont(QFont('Arial', 12,))
        self.lblArrayOrdenado.setText("Array Ordenado com " + self.cboMetodosOrdenacao.currentText() + ":")

        self.lblArrayElementsOrdenado.setFont(QFont('Arial', 12,))
        self.lblArrayElementsOrdenado.setStyleSheet("font-weight: bold")

        for item in auxArray:
            if self.lblArrayElementsOrdenado.text() == "":
                self.lblArrayElementsOrdenado.setText(item)
            else:
                self.lblArrayElementsOrdenado.setText(self.lblArrayElementsOrdenado.text() + ", " + item)

    def isNumber(self):
        try:
            number = int(self.txtNumero.text())
        except Exception:
            self.txtNumero.setText("")

    def setDefaultState(self):
        self.array.clear() #limpar array
        #ui
        self.txtNumero.setEnabled(True)
        self.txtNumero.setFocus()
        self.btnAdd.setEnabled(True)
        self.btnAdd.setStyleSheet("background-color: rgb(255, 255, 255);\n""color: rgb(0, 170, 255);")
        self.btnPronto.setEnabled(True)
        self.btnPronto.setStyleSheet("background-color: rgb(255, 255, 255);\n""color: rgb(0, 170, 255);")
        self.cboMetodosOrdenacao.setEnabled(False)
        self.btnOrdenar.setEnabled(False)
        self.btnOrdenar.setStyleSheet("background-color: rgb(180, 180, 180);\n""color: rgb(0, 170, 255);")
        self.lblArrayElements.setText("")
        self.lblArrayElementsOrdenado.setText("")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmHome = QtWidgets.QMainWindow()
    ui = Ui_FrmHome()
    ui.setupUi(FrmHome)

    FrmHome.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
    FrmHome.setFixedSize(1000, 553)

    FrmHome.show()
    sys.exit(app.exec_())

