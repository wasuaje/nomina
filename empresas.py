# -*- coding: utf-8 -*-

"""
Module implementing Empresas.
"""

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QMainWindow,  QFileDialog,  QPixmap,  QMessageBox
from PyQt4.QtCore import pyqtSignature,   QObject
from PyQt4 import *

from ui.Ui_empresas import Ui_MainWindow

from botonera import Botonera
from  dbdata import *
from busqueda2 import *

class Empresas(QMainWindow, Ui_MainWindow):
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
		#self.botonera.connect(self, QtCore.SIGNAL('on_btnNuevo_released()'), self.on_action_Nuevo_triggered)
		#self.botonera.setupUi(self.frmbotonera)
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
		#self.havedata=False
		self.fill_data()
		#base de datos para controlesQT (tablesview, combos, etc)
		self.db=QDbdata()
		self.ok = self.db.open()
		
		
		self.isediting=False
		self.isadding=False
		
		#self.emit(SIGNAL("btnNuevo_released"), ())		
		self.msgBox=QMessageBox(self)
		self.search=Busqueda(self)	
		self.search.db=self.db
		self.search.campos=['id','nombre', 'rif']
		self.search.tabla='cf_empresa'		
		self.search.headers=['Id','Nombre', 'Rif']		
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
		if self.datos.check_havedata('cf_empresa')==True	:
			self.botonera.btnModificar.setEnabled(True)
			self.botonera.btnEliminar.setEnabled(True)
			self.botonera.btnSearch.setEnabled(True)
			self.botonera.btnPrint.setEnabled(True)				
			self.emp = self.datos.get_data('cf_empresa', id)		
			self.empid=self.emp[0]
			self.lineEdit_2.setText(self.emp[1])
			self.lineEdit_3.setText(self.emp[2])
			self.lineEdit_4.setText(self.emp[3])
			self.lineEdit_5.setText(self.emp[4])
			self.lineEdit_6.setText(self.emp[5])
			self.lineEdit_7.setText(self.emp[6])
			self.lineEdit_8.setText(self.emp[7])
			self.lineEdit.setText(self.emp[8])
		else:
			self.botonera.btnModificar.setEnabled(False)
			self.botonera.btnEliminar.setEnabled(False)
			self.clear_fields()
	
	def clear_fields(self):
		self.lineEdit_2.setText('')
		self.lineEdit_3.setText('')
		self.lineEdit_4.setText('')
		self.lineEdit_5.setText('')
		self.lineEdit_6.setText('')
		self.lineEdit_7.setText('')
		self.lineEdit_8.setText('')
		self.lineEdit.setText('')	

		
	@pyqtSignature("")
	def on_pushButton_released(self):
		"""
		Slot documentation goes here.
		"""
		self.filedialog=QFileDialog.getOpenFileName(self, "Seleccione Archivo", "","*.jpg")		
		self.lineEdit.setText(self.filedialog)
		self.logo=QPixmap()
		self.logo.load(self.filedialog)
		self.label.setPixmap(self.logo) 
		self.msgBox.setText("Imagen cargada con exito !!!")
		self.msgBox.exec_();
		
		#codigo para copiar a la carpeta seleccionada y dialogo todo ok
    

	@pyqtSignature("")
	def on_actionNuevo_triggered(self):
		self.isadding=True
		self.clear_fields()		
		self.frame_2.setEnabled(True)
		self.frame_3.setEnabled(True)
		
	
	@pyqtSignature("")
	def on_actionModificar_triggered(self):		
		self.isediting=True
		self.frame_2.setEnabled(True)
		self.frame_3.setEnabled(True)
#		self.actionGuardar.setEnabled(True)
#		self.actionNuevo.setEnabled(False)
#		self.actionEliminar.setEnabled(False)
#		self.actionModificar.setEnabled(False)

    
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
			datos=['cf_empresa', self.empid]
			rs=self.datos.delete_record(datos)
			if rs:
				self.mensaje='Registro eliminado'
				self.msgBox.setText(self.mensaje)
				self.msgBox.exec_()
				if self.datos.check_havedata('cf_empresa'):
					self.fill_data()
				else:
					self.clear_fields()
	
	@pyqtSignature("")
	def on_actionGuardar_triggered(self):
		"""
		Slot documentation goes here.
		"""        
		#nombre,razon_social,rif,nit,email,tlf,fax,ruta_foto
		if self.isadding:
			datos=[self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text(), self.lineEdit_7.text(), self.lineEdit_8.text(), self.lineEdit.text()]
			self.lastid=self.datos.save_empresa(datos)
			self.mensaje='Datos salvados con exito'			
		elif self.isediting:
			datos=[self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text(), self.lineEdit_7.text(), self.lineEdit_8.text(), self.lineEdit.text(), self.empid]
			self.datos.update_empresa(datos)
			self.lastid=self.empid
			self.mensaje='Datos actualizados con exito'
			
		self.frame_2.setEnabled(False)
		self.frame_3.setEnabled(False)
		self.msgBox.setText(self.mensaje)
		self.msgBox.exec_();
		self.isediting=False
		self.isadding=False
		self.fill_data(self.lastid)

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
		
		



if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	ui = Empresas()
	ui.show()
	sys.exit(app.exec_())
	ui.db.close()	
	ok = self.db.close()		
