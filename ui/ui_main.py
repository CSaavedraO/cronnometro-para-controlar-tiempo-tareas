# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(854, 536)
        MainWindow.setIconSize(QtCore.QSize(28, 28))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnNuevaTarea = QtWidgets.QPushButton(self.centralwidget)
        self.btnNuevaTarea.setGeometry(QtCore.QRect(60, 160, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btnNuevaTarea.setFont(font)
        self.btnNuevaTarea.setStyleSheet("")
        self.btnNuevaTarea.setObjectName("btnNuevaTarea")
        self.btnIniciar = QtWidgets.QPushButton(self.centralwidget)
        self.btnIniciar.setGeometry(QtCore.QRect(710, 470, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btnIniciar.setFont(font)
        self.btnIniciar.setStyleSheet("")
        self.btnIniciar.setObjectName("btnIniciar")
        self.btnDetener = QtWidgets.QPushButton(self.centralwidget)
        self.btnDetener.setGeometry(QtCore.QRect(350, 470, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btnDetener.setFont(font)
        self.btnDetener.setStyleSheet("")
        self.btnDetener.setObjectName("btnDetener")
        self.lblTiempo = QtWidgets.QLabel(self.centralwidget)
        self.lblTiempo.setGeometry(QtCore.QRect(570, 120, 131, 61))
        self.lblTiempo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTiempo.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.lblTiempo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblTiempo.setObjectName("lblTiempo")
        self.qtwTabla = QtWidgets.QTableWidget(self.centralwidget)
        self.qtwTabla.setEnabled(True)
        self.qtwTabla.setGeometry(QtCore.QRect(20, 270, 811, 192))
        font = QtGui.QFont()
        font.setKerning(True)
        self.qtwTabla.setFont(font)
        self.qtwTabla.setAutoScroll(True)
        self.qtwTabla.setTabKeyNavigation(True)
        self.qtwTabla.setProperty("showDropIndicator", True)
        self.qtwTabla.setObjectName("qtwTabla")
        self.qtwTabla.setColumnCount(5)
        self.qtwTabla.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.qtwTabla.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtwTabla.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtwTabla.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtwTabla.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtwTabla.setHorizontalHeaderItem(4, item)
        self.qtwTabla.horizontalHeader().setVisible(True)
        self.qtwTabla.horizontalHeader().setCascadingSectionResizes(False)
        self.qtwTabla.horizontalHeader().setDefaultSectionSize(161)
        self.qtwTabla.horizontalHeader().setMinimumSectionSize(39)
        self.cmbSeleccionartarea = QtWidgets.QComboBox(self.centralwidget)
        self.cmbSeleccionartarea.setGeometry(QtCore.QRect(60, 110, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cmbSeleccionartarea.setFont(font)
        self.cmbSeleccionartarea.setObjectName("cmbSeleccionartarea")
        self.cmbSeleccionartarea.addItem("")
        self.btnCerrarSesion = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.btnCerrarSesion.setGeometry(QtCore.QRect(10, 10, 185, 41))
        self.btnCerrarSesion.setObjectName("btnCerrarSesion")
        self.btnEliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEliminar.setGeometry(QtCore.QRect(240, 470, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btnEliminar.setFont(font)
        self.btnEliminar.setStyleSheet("")
        self.btnEliminar.setObjectName("btnEliminar")
        self.btnPausar = QtWidgets.QPushButton(self.centralwidget)
        self.btnPausar.setGeometry(QtCore.QRect(470, 470, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btnPausar.setFont(font)
        self.btnPausar.setStyleSheet("")
        self.btnPausar.setObjectName("btnPausar")
        self.btnReanudar = QtWidgets.QPushButton(self.centralwidget)
        self.btnReanudar.setGeometry(QtCore.QRect(590, 470, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btnReanudar.setFont(font)
        self.btnReanudar.setStyleSheet("")
        self.btnReanudar.setObjectName("btnReanudar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.qtwTabla.setColumnWidth(0, 150)  
        self.qtwTabla.setColumnWidth(1, 253)  
        self.qtwTabla.setColumnWidth(2, 130)  
        self.qtwTabla.setColumnWidth(3, 130)  
        self.qtwTabla.setColumnWidth(4, 130)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Crono"))
        self.btnNuevaTarea.setText(_translate("MainWindow", "Nueva tarea"))
        self.btnIniciar.setText(_translate("MainWindow", "Iniciar"))
        self.btnDetener.setText(_translate("MainWindow", "Detener"))
        self.lblTiempo.setText(_translate("MainWindow", "00:00:00"))
        item = self.qtwTabla.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.qtwTabla.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Descripcion"))
        item = self.qtwTabla.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tiempos"))
        item = self.qtwTabla.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Clasificacion"))
        item = self.qtwTabla.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Estado"))
        self.cmbSeleccionartarea.setItemText(0, _translate("MainWindow", "Seleccionar tarea"))
        self.btnCerrarSesion.setText(_translate("MainWindow", "Cerrar Sesión"))
        self.btnEliminar.setText(_translate("MainWindow", "Eliminar"))
        self.btnPausar.setText(_translate("MainWindow", "Pausar"))
        self.btnReanudar.setText(_translate("MainWindow", "Reanudar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
