# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Signup(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(555, 529)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblSignup = QtWidgets.QLabel(self.centralwidget)
        self.lblSignup.setGeometry(QtCore.QRect(180, 30, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.lblSignup.setFont(font)
        self.lblSignup.setObjectName("lblSignup")
        self.lblNombre = QtWidgets.QLabel(self.centralwidget)
        self.lblNombre.setGeometry(QtCore.QRect(30, 120, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.lblNombre.setFont(font)
        self.lblNombre.setObjectName("lblNombre")
        self.lblApellido = QtWidgets.QLabel(self.centralwidget)
        self.lblApellido.setGeometry(QtCore.QRect(290, 110, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.lblApellido.setFont(font)
        self.lblApellido.setObjectName("lblApellido")
        self.lblConfirmar = QtWidgets.QLabel(self.centralwidget)
        self.lblConfirmar.setGeometry(QtCore.QRect(290, 340, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.lblConfirmar.setFont(font)
        self.lblConfirmar.setObjectName("lblConfirmar")
        self.lblContrasena2 = QtWidgets.QLabel(self.centralwidget)
        self.lblContrasena2.setGeometry(QtCore.QRect(20, 340, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.lblContrasena2.setFont(font)
        self.lblContrasena2.setObjectName("lblContrasena2")
        self.lblCorreo2 = QtWidgets.QLabel(self.centralwidget)
        self.lblCorreo2.setGeometry(QtCore.QRect(30, 230, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.lblCorreo2.setFont(font)
        self.lblCorreo2.setObjectName("lblCorreo2")
        self.btnIngresar_regis = QtWidgets.QPushButton(self.centralwidget)
        self.btnIngresar_regis.setGeometry(QtCore.QRect(40, 450, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btnIngresar_regis.setFont(font)
        self.btnIngresar_regis.setStyleSheet("")
        self.btnIngresar_regis.setObjectName("btnIngresar_regis")
        self.txtnombre_regis = QtWidgets.QLineEdit(self.centralwidget)
        self.txtnombre_regis.setGeometry(QtCore.QRect(20, 170, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtnombre_regis.setFont(font)
        self.txtnombre_regis.setStyleSheet("")
        self.txtnombre_regis.setObjectName("txtnombre_regis")
        self.txtapellido_regis = QtWidgets.QLineEdit(self.centralwidget)
        self.txtapellido_regis.setGeometry(QtCore.QRect(270, 170, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtapellido_regis.setFont(font)
        self.txtapellido_regis.setStyleSheet("")
        self.txtapellido_regis.setObjectName("txtapellido_regis")
        self.txtcorreo_regis = QtWidgets.QLineEdit(self.centralwidget)
        self.txtcorreo_regis.setGeometry(QtCore.QRect(30, 270, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtcorreo_regis.setFont(font)
        self.txtcorreo_regis.setStyleSheet("")
        self.txtcorreo_regis.setObjectName("txtcorreo_regis")
        self.txtconstrasena_regis = QtWidgets.QLineEdit(self.centralwidget)
        self.txtconstrasena_regis.setGeometry(QtCore.QRect(20, 390, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtconstrasena_regis.setFont(font)
        self.txtconstrasena_regis.setStyleSheet("")
        self.txtconstrasena_regis.setObjectName("txtconstrasena_regis")
        self.txtcontrasenaconfir_regis = QtWidgets.QLineEdit(self.centralwidget)
        self.txtcontrasenaconfir_regis.setGeometry(QtCore.QRect(270, 390, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtcontrasenaconfir_regis.setFont(font)
        self.txtcontrasenaconfir_regis.setStyleSheet("")
        self.txtcontrasenaconfir_regis.setObjectName("txtcontrasenaconfir_regis")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(300, 450, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btnCancelar.setFont(font)
        self.btnCancelar.setStyleSheet("")
        self.btnCancelar.setObjectName("btnCancelar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sign Up"))
        self.lblSignup.setText(_translate("MainWindow", "SIGN UP"))
        self.lblNombre.setText(_translate("MainWindow", "Nombre"))
        self.lblApellido.setText(_translate("MainWindow", "Apellido"))
        self.lblConfirmar.setText(_translate("MainWindow", "Confirmar contraseña"))
        self.lblContrasena2.setText(_translate("MainWindow", "Contraseña"))
        self.lblCorreo2.setText(_translate("MainWindow", "Correo"))
        self.btnIngresar_regis.setText(_translate("MainWindow", "Ingresar"))
        self.btnCancelar.setText(_translate("MainWindow", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Signup()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
