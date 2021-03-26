# -*- coding: utf-8 -*-

"""
Module implementing Cargos.
"""

from PyQt4.QtGui import QMainWindow,  QPixmap,  QMessageBox
from PyQt4.QtCore import pyqtSignature
from PyQt4 import *

from ui.Ui_nomina_tipo import Ui_MainWindow

from  dbdata import *
from busqueda2 import *
from botonera import Botonera


class NominaTipo(QMainWindow, Ui_MainWindow):
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
		#self.havedata=False
		self.fill_data()
		
		self.isediting=False
		self.isadding=False
		
		#self.emit(SIGNAL("btnNuevo_released"), ())		
		self.msgBox=QMessageBox(self)
		self.search=Busqueda(self)		
		self.search.campos=['id','nombre']
		self.search.tabla='cf_nomina_tipo'		
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
		if self.datos.check_havedata('cf_nomina_tipo')==True	:
			self.botonera.btnModificar.setEnabled(True)
			self.botonera.btnEliminar.setEnabled(True)
			self.botonera.btnSearch.setEnabled(True)
			self.botonera.btnPrint.setEnabled(True)				
			self.emp = self.datos.get_data('cf_nomina_tipo', id)		
			self.empid=self.emp[0]
			self.lnnombre.setText(self.emp[1])
			self.lndias.setText(str(self.emp[2]))
			self.lnperiodos.setText(str(self.emp[3]))
			
		else:
			self.botonera.btnModificar.setEnabled(False)
			self.botonera.btnEliminar.setEnabled(False)
			self.clear_fields()
	
	def clear_fields(self):		
		self.lnnombre.setText('')
		self.lndias.setText('')
		self.lnperiodos.setText('')
		
	
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
			datos=['cf_nomina_tipo', self.empid]
			rs=self.datos.delete_record(datos)
			if rs:
				self.mensaje='Registro eliminado'
				self.msgBox.setText(self.mensaje)
				self.msgBox.exec_()
				if self.datos.check_havedata('cf_nomina_tipo'):
					self.fill_data()
				else:
					self.clear_fields()
					
	@pyqtSignature("")
	def on_actionGuardar_triggered(self):
		"""
        Slot documentation goes here.
        """
		if self.isadding:
			datos=[self.lnnombre.text(), self.lndias.text(),self.lnperiodos.text()]
			self.lastid=self.datos.save_nomina_tipo(datos)
			self.mensaje='Datos salvados con exito'			
		elif self.isediting:
			datos=[self.lnnombre.text(), self.lndias.text(),self.lnperiodos.text(), self.empid]
			self.datos.update_nomina_tipo(datos)
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
    ui = NominaTipo()
    ui.show()
    sys.exit(app.exec_())
