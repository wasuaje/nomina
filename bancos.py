# -*- coding: utf-8 -*-

"""
Module implementing Cargos.
"""

from PyQt4.QtGui import QMainWindow,  QPixmap,  QMessageBox
from PyQt4.QtCore import pyqtSignature
from PyQt4 import *
from PyQt4.QtSql import *

from ui.Ui_bancos import Ui_MainWindow

from  dbdata import *
from busqueda2 import *
from botonera import Botonera


class Bancos(QMainWindow, Ui_MainWindow):
	"""
	Class documentation goes here.
	"""
	def __init__(self, parent = None):
		"""
		Constructor
		"""
		QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.botonera=Botonera(self.frmbotonera)
		self.connect(self.botonera, QtCore.SIGNAL("btnNuevo_released"),    
                        self.on_actionNuevo_triggered)
		self.connect(self.botonera, QtCore.SIGNAL("btnModificar_released"),    
                        self.on_actionModificar_triggered)
		self.connect(self.botonera, QtCore.SIGNAL("btnGuardar_released"),    
                        self.on_actionGuardar_triggered)						
		self.connect(self.botonera, QtCore.SIGNAL("btnSalir_released"),    
                        self.on_actionSalir_triggered)
		self.connect(self.botonera, QtCore.SIGNAL("btnSearch_released"),    
                        self.show_search)
		self.connect(self.botonera, QtCore.SIGNAL("btnEliminar_released"),    
                        self.on_actionEliminar_triggered)
						

		self.datos=Dbdata()		
		
		self.db=QDbdata()
		ok = self.db.open()
		self.model = QSqlQueryModel(self)
		self.headersdet = ['Id','Cuenta',  'Numero']		

		self.fill_data()

		self.isediting=False
		self.isadding=False
		
		self.msgBox=QMessageBox(self)
		self.search=Busqueda(self)		
		self.search.db=self.db
		self.search.campos=['id','nombre']
		self.search.tabla='cf_banco'		
		self.search.headers=['Id','Nombre']		
		self.search.sql='select '+ ','.join(self.search.campos) + ' from '+self.search.tabla 
		self.connect(self.search, QtCore.SIGNAL("tableView_clicked"), self.fill_data)

	def show_search(self):				
		self.search.fillgrid()
		self.search.show()
	
	def fill_data(self, id=None):				
				#id.model().record(id.row()).value('id').toInt()		
		#if id !=None:			
		#	id = id.model().record(id.row()).value('id').toInt()
		#	id = id[0]		#solo para enteros para string cambia
		if self.datos.check_havedata('cf_banco')==True	:
			self.botonera.btnModificar.setEnabled(True)
			self.botonera.btnEliminar.setEnabled(True)
			self.botonera.btnSearch.setEnabled(True)
			self.botonera.btnPrint.setEnabled(True)				
			self.emp = self.datos.get_data('cf_banco', id)		
			self.empid=self.emp[0]
			self.lineEdit.setText(self.emp[1])
			self.fillgrid()
		else:
			self.botonera.btnModificar.setEnabled(False)
			self.botonera.btnEliminar.setEnabled(False)
			self.clear_fields()
	
	def clear_fields(self):
		self.lineEdit.setText('')
		
	def fillgrid(self):				
		self.sqldet = 'select id, nombre, cuenta from cf_banco_cuenta where cf_banco_id ='+str(self.empid)
		self.model.setQuery(self.sqldet);		
		for i in range(0, len(self.headersdet)):
			self.model.setHeaderData(i, Qt.Horizontal, self.headersdet[i])
			self.model.setHeaderData(i, Qt.Horizontal, self.headersdet[i])
		self.tableView.setModel(self.model)
		self.tableView.setColumnHidden(0, True)
		self.tableView.setColumnWidth ( 1, 165 )
		self.tableView.setColumnWidth ( 2, 185 )
		self.tableView.show()


	@pyqtSignature("")
	def on_actionNuevo_triggered(self):
		self.isadding=True
		self.clear_fields()
		self.tabWidget.setEnabled(True)
    
	@pyqtSignature("")
	def on_actionModificar_triggered(self):
		self.isediting=True
		self.tabWidget.setEnabled(True)
		
	@pyqtSignature("")
	def on_actionEliminar_triggered(self):
		"""
		Slot documentation goes here.
		"""
		self.msgBox.setText('Esta seguro de eliminar registro?')
		self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
		self.msgBox.setDefaultButton(QMessageBox.Cancel)
		result=self.msgBox.exec_()		
		#print sssss
		if result == QMessageBox.Ok:			
			datos=['cf_banco', self.empid]
			rs=self.datos.delete_record(datos)
			if rs:
				self.mensaje='Registro eliminado'
				self.msgBox.setText(self.mensaje)
				self.msgBox.exec_()
				if self.datos.check_havedata('cf_banco'):
					self.fill_data()
				else:
					self.clear_fields()
					
	@pyqtSignature("")
	def on_actionGuardar_triggered(self):
		"""
        Slot documentation goes here.
        """
		if self.isadding:
			datos=[self.lineEdit.text()]
			self.lastid=self.datos.save_banco(datos)
			self.mensaje='Datos salvados con exito'			
		elif self.isediting:
			datos=[self.lineEdit.text(), self.empid]
			self.datos.update_banco(datos)
			self.lastid=self.empid
			self.mensaje='Datos actualizados con exito'
			
		#print 'last id'+str(self.lastid)
		self.tabWidget.setEnabled(False)
		self.msgBox.setText(self.mensaje)
		self.msgBox.exec_();
		self.isediting=False
		self.isadding=False
		self.fill_data(self.lastid)

	@pyqtSignature("")
	def on_pushAdd_released(self):
		"""
		Slot documentation goes here.
		"""
		if self.isediting:
			if len(self.linecta.text()) > 0 and len(self.linenro.text()) > 0:
				datos=[self.linecta.text(), self.linenro.text(), self.empid]
				self.lastdetid=self.datos.save_cuenta(datos)
				if self.lastdetid > 0:	
					self.linecta.setText('')
					self.linenro.setText('')
					self.fillgrid()				
			else:
				self.mensaje='Debe llenar los campos requeridos'
				self.msgBox.setText(self.mensaje)
				self.msgBox.exec_()
		else:
				self.mensaje='Funcion disponible solo en modo edicion'
				self.msgBox.setText(self.mensaje)
				self.msgBox.exec_();
			
	@pyqtSignature("")
	def on_pushdel_released(self):
		"""
		Slot documentation goes here.
		"""
		if self.isediting:			
			datos=['cf_banco_cuenta', self.idtodelete[0]]
			rs=self.datos.delete_record(datos)
			self.fillgrid()
		else:
			self.mensaje='Funcion disponible solo en modo edicion'
			self.msgBox.setText(self.mensaje)
			self.msgBox.exec_();
		self.pushdel.setEnabled(False)
		
	@pyqtSignature("QModelIndex")
	def on_tableView_clicked(self, index):
		"""
		Slot documentation goes here.
		"""
		self.idtodelete =  self.model.record(index.row()).value('id').toInt()
		self.pushdel.setEnabled(True)

	@pyqtSignature("")
	def on_actionSalir_triggered(self):
		"""
        Slot documentation goes here.
        """		
		self.msgBox.setText('Esta seguro que desea salir?')
		self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
		self.msgBox.setDefaultButton(QMessageBox.Cancel)
		result=self.msgBox.exec_()				
		if result == QMessageBox.Ok:	
			self.close()
		else:
			pass
			
import recurso_rc			
			
if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	ui = Bancos()
	ui.show()	
	sys.exit(app.exec_())
	ui.db.close()	
	ok = self.db.close()		


