# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wasuaje/Documentos/desarrollo/nomina/ui/bancos.ui'
#
# Created: Thu Jul 14 12:02:43 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(450, 439)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(500, 600))
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 431, 411))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.frmbotonera = QtGui.QFrame(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmbotonera.sizePolicy().hasHeightForWidth())
        self.frmbotonera.setSizePolicy(sizePolicy)
        self.frmbotonera.setMinimumSize(QtCore.QSize(50, 40))
        self.frmbotonera.setFrameShape(QtGui.QFrame.NoFrame)
        self.frmbotonera.setFrameShadow(QtGui.QFrame.Raised)
        self.frmbotonera.setObjectName(_fromUtf8("frmbotonera"))
        self.verticalLayout_5.addWidget(self.frmbotonera)
        spacerItem = QtGui.QSpacerItem(2, 2, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem)
        self.tabWidget = QtGui.QTabWidget(self.layoutWidget)
        self.tabWidget.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(70, 20, 311, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 20, 51, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.linecta = QtGui.QLineEdit(self.tab)
        self.linecta.setGeometry(QtCore.QRect(70, 50, 111, 27))
        self.linecta.setObjectName(_fromUtf8("linecta"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 51, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tableView = QtGui.QTableView(self.tab)
        self.tableView.setGeometry(QtCore.QRect(10, 90, 371, 231))
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView.horizontalHeader().setMinimumSectionSize(40)
        self.pushAdd = QtGui.QPushButton(self.tab)
        self.pushAdd.setGeometry(QtCore.QRect(390, 90, 31, 27))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos2/img2/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushAdd.setIcon(icon)
        self.pushAdd.setFlat(True)
        self.pushAdd.setObjectName(_fromUtf8("pushAdd"))
        self.pushdel = QtGui.QPushButton(self.tab)
        self.pushdel.setEnabled(False)
        self.pushdel.setGeometry(QtCore.QRect(390, 120, 31, 27))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos2/img2/cross.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushdel.setIcon(icon1)
        self.pushdel.setFlat(True)
        self.pushdel.setObjectName(_fromUtf8("pushdel"))
        self.linenro = QtGui.QLineEdit(self.tab)
        self.linenro.setGeometry(QtCore.QRect(230, 50, 151, 27))
        self.linenro.setObjectName(_fromUtf8("linenro"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(190, 50, 41, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.verticalLayout_5.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 450, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuNuevo = QtGui.QMenu(self.menuBar)
        self.menuNuevo.setObjectName(_fromUtf8("menuNuevo"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionNuevo = QtGui.QAction(MainWindow)
        self.actionNuevo.setObjectName(_fromUtf8("actionNuevo"))
        self.actionModificar = QtGui.QAction(MainWindow)
        self.actionModificar.setObjectName(_fromUtf8("actionModificar"))
        self.actionEliminar = QtGui.QAction(MainWindow)
        self.actionEliminar.setObjectName(_fromUtf8("actionEliminar"))
        self.actionGuardar = QtGui.QAction(MainWindow)
        self.actionGuardar.setObjectName(_fromUtf8("actionGuardar"))
        self.actionSalir = QtGui.QAction(MainWindow)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.menuNuevo.addAction(self.actionNuevo)
        self.menuNuevo.addAction(self.actionModificar)
        self.menuNuevo.addAction(self.actionGuardar)
        self.menuNuevo.addAction(self.actionEliminar)
        self.menuNuevo.addSeparator()
        self.menuNuevo.addAction(self.actionSalir)
        self.menuBar.addAction(self.menuNuevo.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.linecta)
        MainWindow.setTabOrder(self.linecta, self.linenro)
        MainWindow.setTabOrder(self.linenro, self.pushAdd)
        MainWindow.setTabOrder(self.pushAdd, self.pushdel)
        MainWindow.setTabOrder(self.pushdel, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.tableView)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Bancos", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Banco:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Cuenta:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Nro.:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Datos", None, QtGui.QApplication.UnicodeUTF8))
        self.menuNuevo.setTitle(QtGui.QApplication.translate("MainWindow", "&Archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevo.setText(QtGui.QApplication.translate("MainWindow", "Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionModificar.setText(QtGui.QApplication.translate("MainWindow", "Modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEliminar.setText(QtGui.QApplication.translate("MainWindow", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGuardar.setText(QtGui.QApplication.translate("MainWindow", "Guardar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setText(QtGui.QApplication.translate("MainWindow", "Salir", None, QtGui.QApplication.UnicodeUTF8))

import recurso_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

