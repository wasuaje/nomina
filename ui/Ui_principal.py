# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wasuaje/Documentos/desarrollo/nomina/ui/principal.ui'
#
# Created: Thu Jul 14 12:02:38 2011
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
        MainWindow.resize(818, 724)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 170, 331, 251))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../img/emp/Cuenta_nomina.jpg")))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArchivo = QtGui.QMenu(self.menubar)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
        self.menuConfigurar = QtGui.QMenu(self.menubar)
        self.menuConfigurar.setObjectName(_fromUtf8("menuConfigurar"))
        self.menuMovimientos = QtGui.QMenu(self.menubar)
        self.menuMovimientos.setObjectName(_fromUtf8("menuMovimientos"))
        self.menuEmpleados = QtGui.QMenu(self.menuMovimientos)
        self.menuEmpleados.setObjectName(_fromUtf8("menuEmpleados"))
        self.menuNomina = QtGui.QMenu(self.menuMovimientos)
        self.menuNomina.setObjectName(_fromUtf8("menuNomina"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menuReportes = QtGui.QMenu(self.menubar)
        self.menuReportes.setObjectName(_fromUtf8("menuReportes"))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.action_Empresa = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/img/home_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Empresa.setIcon(icon)
        self.action_Empresa.setIconVisibleInMenu(True)
        self.action_Empresa.setObjectName(_fromUtf8("action_Empresa"))
        self.action_Departamentos = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/img/activity_monitor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Departamentos.setIcon(icon1)
        self.action_Departamentos.setObjectName(_fromUtf8("action_Departamentos"))
        self.actionCargos = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/img/address_book_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCargos.setIcon(icon2)
        self.actionCargos.setObjectName(_fromUtf8("actionCargos"))
        self.action_Bancos_cuentas = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/img/window_app_list_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Bancos_cuentas.setIcon(icon3)
        self.action_Bancos_cuentas.setObjectName(_fromUtf8("action_Bancos_cuentas"))
        self.action_Tipos_de_Nomina = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/img/book_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Tipos_de_Nomina.setIcon(icon4)
        self.action_Tipos_de_Nomina.setObjectName(_fromUtf8("action_Tipos_de_Nomina"))
        self.actionTipos_de_Empleado = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/img/users_business_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTipos_de_Empleado.setIcon(icon5)
        self.actionTipos_de_Empleado.setObjectName(_fromUtf8("actionTipos_de_Empleado"))
        self.actionEmpleados = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/img/user_business_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEmpleados.setIcon(icon6)
        self.actionEmpleados.setObjectName(_fromUtf8("actionEmpleados"))
        self.action_Salir = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/img/close_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Salir.setIcon(icon7)
        self.action_Salir.setIconVisibleInMenu(True)
        self.action_Salir.setObjectName(_fromUtf8("action_Salir"))
        self.actionAusencias = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/img/user_business_close_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAusencias.setIcon(icon8)
        self.actionAusencias.setObjectName(_fromUtf8("actionAusencias"))
        self.actionPrestamos = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/img/user_business_chart_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrestamos.setIcon(icon9)
        self.actionPrestamos.setObjectName(_fromUtf8("actionPrestamos"))
        self.actionVacaciones = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/img/user_business_info_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVacaciones.setIcon(icon10)
        self.actionVacaciones.setObjectName(_fromUtf8("actionVacaciones"))
        self.actionTipos_de_Concepto = QtGui.QAction(MainWindow)
        self.actionTipos_de_Concepto.setObjectName(_fromUtf8("actionTipos_de_Concepto"))
        self.actionConceptos = QtGui.QAction(MainWindow)
        self.actionConceptos.setObjectName(_fromUtf8("actionConceptos"))
        self.actionVariaciones = QtGui.QAction(MainWindow)
        self.actionVariaciones.setObjectName(_fromUtf8("actionVariaciones"))
        self.actionGenerar_Nomina = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/img/page_table_add_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGenerar_Nomina.setIcon(icon11)
        self.actionGenerar_Nomina.setObjectName(_fromUtf8("actionGenerar_Nomina"))
        self.action_Acerca = QtGui.QAction(MainWindow)
        self.action_Acerca.setObjectName(_fromUtf8("action_Acerca"))
        self.actionConceptos_por_Nomina = QtGui.QAction(MainWindow)
        self.actionConceptos_por_Nomina.setObjectName(_fromUtf8("actionConceptos_por_Nomina"))
        self.actionBasicos = QtGui.QAction(MainWindow)
        self.actionBasicos.setObjectName(_fromUtf8("actionBasicos"))
        self.actionNomina_2 = QtGui.QAction(MainWindow)
        self.actionNomina_2.setObjectName(_fromUtf8("actionNomina_2"))
        self.menuArchivo.addAction(self.action_Salir)
        self.menuConfigurar.addAction(self.action_Empresa)
        self.menuConfigurar.addAction(self.action_Departamentos)
        self.menuConfigurar.addAction(self.actionCargos)
        self.menuConfigurar.addSeparator()
        self.menuConfigurar.addAction(self.action_Bancos_cuentas)
        self.menuConfigurar.addSeparator()
        self.menuConfigurar.addAction(self.actionTipos_de_Empleado)
        self.menuConfigurar.addAction(self.actionEmpleados)
        self.menuEmpleados.addSeparator()
        self.menuEmpleados.addAction(self.actionAusencias)
        self.menuEmpleados.addAction(self.actionPrestamos)
        self.menuEmpleados.addAction(self.actionVacaciones)
        self.menuNomina.addAction(self.action_Tipos_de_Nomina)
        self.menuNomina.addAction(self.actionTipos_de_Concepto)
        self.menuNomina.addAction(self.actionConceptos)
        self.menuNomina.addAction(self.actionConceptos_por_Nomina)
        self.menuNomina.addAction(self.actionVariaciones)
        self.menuNomina.addAction(self.actionGenerar_Nomina)
        self.menuMovimientos.addAction(self.menuEmpleados.menuAction())
        self.menuMovimientos.addAction(self.menuNomina.menuAction())
        self.menu.addAction(self.action_Acerca)
        self.menuReportes.addAction(self.actionBasicos)
        self.menuReportes.addAction(self.actionNomina_2)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuConfigurar.menuAction())
        self.menubar.addAction(self.menuMovimientos.menuAction())
        self.menubar.addAction(self.menuReportes.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.toolBar.addAction(self.action_Empresa)
        self.toolBar.addAction(self.action_Departamentos)
        self.toolBar.addAction(self.actionCargos)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuArchivo.setTitle(QtGui.QApplication.translate("MainWindow", "&Archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.menuConfigurar.setTitle(QtGui.QApplication.translate("MainWindow", "&Configuracion", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMovimientos.setTitle(QtGui.QApplication.translate("MainWindow", "&Movimientos", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEmpleados.setTitle(QtGui.QApplication.translate("MainWindow", "&Empleados", None, QtGui.QApplication.UnicodeUTF8))
        self.menuNomina.setTitle(QtGui.QApplication.translate("MainWindow", "&Nomina", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setTitle(QtGui.QApplication.translate("MainWindow", "&?", None, QtGui.QApplication.UnicodeUTF8))
        self.menuReportes.setTitle(QtGui.QApplication.translate("MainWindow", "&Reportes", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Empresa.setText(QtGui.QApplication.translate("MainWindow", "&Empresa", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Departamentos.setText(QtGui.QApplication.translate("MainWindow", "&Departamentos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCargos.setText(QtGui.QApplication.translate("MainWindow", "&Cargos", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Bancos_cuentas.setText(QtGui.QApplication.translate("MainWindow", "&Bancos/cuentas", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Tipos_de_Nomina.setText(QtGui.QApplication.translate("MainWindow", "&Tipos de Nomina", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTipos_de_Empleado.setText(QtGui.QApplication.translate("MainWindow", "T&ipos de Empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEmpleados.setText(QtGui.QApplication.translate("MainWindow", "E&mpleados", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Salir.setText(QtGui.QApplication.translate("MainWindow", "&Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAusencias.setText(QtGui.QApplication.translate("MainWindow", "&Ausencias", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrestamos.setText(QtGui.QApplication.translate("MainWindow", "&Prestamos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVacaciones.setText(QtGui.QApplication.translate("MainWindow", "&Vacaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTipos_de_Concepto.setText(QtGui.QApplication.translate("MainWindow", "T&ipos de Concepto", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConceptos.setText(QtGui.QApplication.translate("MainWindow", "&Conceptos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVariaciones.setText(QtGui.QApplication.translate("MainWindow", "&Variaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGenerar_Nomina.setText(QtGui.QApplication.translate("MainWindow", "&Generar Nomina", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Acerca.setText(QtGui.QApplication.translate("MainWindow", "&Acerca", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConceptos_por_Nomina.setText(QtGui.QApplication.translate("MainWindow", "Conceptos por Nomina", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBasicos.setText(QtGui.QApplication.translate("MainWindow", "Basicos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNomina_2.setText(QtGui.QApplication.translate("MainWindow", "Nomina", None, QtGui.QApplication.UnicodeUTF8))

import recurso_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

