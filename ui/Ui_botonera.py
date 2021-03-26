# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wasuaje/Documentos/desarrollo/nomina/ui/botonera.ui'
#
# Created: Thu Jul 14 12:02:40 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(372, 43)
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.horizontalLayoutWidget_4 = QtGui.QWidget(Form)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 387, 44))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnNuevo = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.btnNuevo.setMouseTracking(False)
        self.btnNuevo.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/img/page_text_add_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNuevo.setIcon(icon)
        self.btnNuevo.setIconSize(QtCore.QSize(32, 32))
        self.btnNuevo.setCheckable(False)
        self.btnNuevo.setFlat(True)
        self.btnNuevo.setObjectName(_fromUtf8("btnNuevo"))
        self.horizontalLayout_2.addWidget(self.btnNuevo)
        self.btnGuardar = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.btnGuardar.setEnabled(False)
        self.btnGuardar.setMouseTracking(False)
        self.btnGuardar.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/img/save_download_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGuardar.setIcon(icon1)
        self.btnGuardar.setIconSize(QtCore.QSize(32, 32))
        self.btnGuardar.setCheckable(False)
        self.btnGuardar.setFlat(True)
        self.btnGuardar.setObjectName(_fromUtf8("btnGuardar"))
        self.horizontalLayout_2.addWidget(self.btnGuardar)
        self.btnModificar = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.btnModificar.setEnabled(False)
        self.btnModificar.setMouseTracking(False)
        self.btnModificar.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/img/pencil_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModificar.setIcon(icon2)
        self.btnModificar.setIconSize(QtCore.QSize(32, 32))
        self.btnModificar.setCheckable(False)
        self.btnModificar.setFlat(True)
        self.btnModificar.setObjectName(_fromUtf8("btnModificar"))
        self.horizontalLayout_2.addWidget(self.btnModificar)
        self.btnEliminar = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.btnEliminar.setEnabled(False)
        self.btnEliminar.setMouseTracking(False)
        self.btnEliminar.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/img/page_blank_close_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEliminar.setIcon(icon3)
        self.btnEliminar.setIconSize(QtCore.QSize(32, 32))
        self.btnEliminar.setCheckable(False)
        self.btnEliminar.setFlat(True)
        self.btnEliminar.setObjectName(_fromUtf8("btnEliminar"))
        self.horizontalLayout_2.addWidget(self.btnEliminar)
        self.line_2 = QtGui.QFrame(self.horizontalLayoutWidget_4)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_2.addWidget(self.line_2)
        self.btnSearch = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.btnSearch.setEnabled(False)
        self.btnSearch.setMouseTracking(False)
        self.btnSearch.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/img/search_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSearch.setIcon(icon4)
        self.btnSearch.setIconSize(QtCore.QSize(32, 32))
        self.btnSearch.setCheckable(False)
        self.btnSearch.setFlat(True)
        self.btnSearch.setObjectName(_fromUtf8("btnSearch"))
        self.horizontalLayout_2.addWidget(self.btnSearch)
        self.btnPrint = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.btnPrint.setEnabled(False)
        self.btnPrint.setMouseTracking(False)
        self.btnPrint.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/img/page_text_chart_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPrint.setIcon(icon5)
        self.btnPrint.setIconSize(QtCore.QSize(32, 32))
        self.btnPrint.setCheckable(False)
        self.btnPrint.setFlat(True)
        self.btnPrint.setObjectName(_fromUtf8("btnPrint"))
        self.horizontalLayout_2.addWidget(self.btnPrint)
        self.line = QtGui.QFrame(self.horizontalLayoutWidget_4)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_2.addWidget(self.line)
        self.btnSalir = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.btnSalir.setMouseTracking(False)
        self.btnSalir.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/img/close_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalir.setIcon(icon6)
        self.btnSalir.setIconSize(QtCore.QSize(32, 32))
        self.btnSalir.setCheckable(False)
        self.btnSalir.setFlat(True)
        self.btnSalir.setObjectName(_fromUtf8("btnSalir"))
        self.horizontalLayout_2.addWidget(self.btnSalir)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))

import recurso_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

