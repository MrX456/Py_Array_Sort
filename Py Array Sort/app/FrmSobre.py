# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmSobre.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FrmSobre(object):
    def setupUi(self, FrmSobre):
        FrmSobre.setObjectName("FrmSobre")
        FrmSobre.resize(388, 181)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrmSobre.setWindowIcon(icon)
        self.frame = QtWidgets.QFrame(FrmSobre)
        self.frame.setGeometry(QtCore.QRect(0, 0, 391, 191))
        self.frame.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lblTitle = QtWidgets.QLabel(self.frame)
        self.lblTitle.setGeometry(QtCore.QRect(140, 20, 111, 31))
        self.lblTitle.setObjectName("lblTitle")
        self.lblVersion = QtWidgets.QLabel(self.frame)
        self.lblVersion.setGeometry(QtCore.QRect(150, 60, 91, 16))
        self.lblVersion.setObjectName("lblVersion")
        self.lblPython = QtWidgets.QLabel(self.frame)
        self.lblPython.setGeometry(QtCore.QRect(120, 90, 151, 20))
        self.lblPython.setObjectName("lblPython")
        self.lblDeveloper = QtWidgets.QLabel(self.frame)
        self.lblDeveloper.setGeometry(QtCore.QRect(120, 120, 151, 20))
        self.lblDeveloper.setObjectName("lblDeveloper")
        self.btnOK = QtWidgets.QPushButton(self.frame)
        self.btnOK.setGeometry(QtCore.QRect(160, 150, 75, 23))
        self.btnOK.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnOK.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 255);")
        self.btnOK.setObjectName("btnOK")

        self.retranslateUi(FrmSobre)
        QtCore.QMetaObject.connectSlotsByName(FrmSobre)

    def retranslateUi(self, FrmSobre):
        _translate = QtCore.QCoreApplication.translate
        FrmSobre.setWindowTitle(_translate("FrmSobre", "Sobre o Py Array Sort"))
        self.lblTitle.setText(_translate("FrmSobre", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Py Array Sort</span></p></body></html>"))
        self.lblVersion.setText(_translate("FrmSobre", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Versão : 1.0.0</span></p></body></html>"))
        self.lblPython.setText(_translate("FrmSobre", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Versão do Python : 3.4.3</span></p></body></html>"))
        self.lblDeveloper.setText(_translate("FrmSobre", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Desenvolvido por : MrX</span></p></body></html>"))
        self.btnOK.setText(_translate("FrmSobre", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmSobre = QtWidgets.QDialog()
    ui = Ui_FrmSobre()
    ui.setupUi(FrmSobre)
    FrmSobre.show()
    sys.exit(app.exec_())

