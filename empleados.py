# -*- coding: utf-8 -*-

"""
Module implementing Cargos.
"""

from PyQt4.QtGui import QMainWindow,  QPixmap,  QMessageBox,  QDoubleValidator,  QFileDialog
from PyQt4.QtCore import pyqtSignature,  QVariant,  QDate
from PyQt4 import *
from PyQt4.QtSql import *

from ui.Ui_empleados import Ui_MainWindow
import os, datetime, shutil
from  dbdata import *
from busqueda2 import *
from botonera import Botonera


class Empleados(QMainWindow, Ui_MainWindow):
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
						
		#base de datos para uso normal
		self.datos=Dbdata()		
		#base de datos para controlesQT (tablesview, combos, etc)
		self.db=QDbdata()
		self.ok = self.db.open()
		self.model = QSqlQueryModel(self)
		self.model2 = QSqlQueryModel(self)
		
		self.headersdet = ['Id','Fecha Valido',  'Mensual',  'Semanal',   'Diario']		

		#coloco algunos id en 0
		self.idcargo=0
		self.tipemp=0
		self.iddpto=0
		self.idtiponom=0
		self.idbanco=0
		
		self.fill_data()

		self.isediting=False
		self.isadding=False
		
		#los valores necesario para que el popup de busqueda funcione y luego instanciarlo
		self.msgBox=QMessageBox(self)		
		self.search=Busqueda(self)		
		self.search.db=self.db
		self.search.campos=['id','cedula', 'nombres','apellidos']
		self.search.tabla='cf_empleado'		
		self.search.headers=['Id', 'Cedula','Nombres', 'Apellidos']		
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
		
		if self.datos.check_havedata('cf_empleado')==True	:
			self.botonera.btnModificar.setEnabled(True)
			self.botonera.btnEliminar.setEnabled(True)
			self.botonera.btnSearch.setEnabled(True)
			self.botonera.btnPrint.setEnabled(True)				
			self.emp = self.datos.get_data('cf_empleado', id)		
			#algunas tanformaciones para las fechas para usar el control dateedit		
			
			self.empid=self.emp[0]
			self.lncodigo.setText(self.emp[1])
			self.lnsexo.setText(self.emp[2])
			self.lnnombres.setText(self.emp[3])
			self.lnapellidos.setText(self.emp[4])		
			self.lncedula.setText(str(self.emp[5]))
			self.lnrif.setText(self.emp[6])
			self.lntlfhab.setText(self.emp[7])
			self.lntlfcel.setText(self.emp[8])
			if self.emp[9] == None:
				self.lnfecnac.setDate(QDate(1, 1, 1900))
			else:
				self.lnfecnac.setDate(self.emp[9])
				
			self.txtdir1.setPlainText(self.emp[10])
			self.txtdir2.setPlainText(self.emp[11])
			self.lnemail.setText(self.emp[12])			
			if self.emp[13] == None:
				self.lnfecingreso.setDate(QDate(1, 1, 1900))
			else:
				self.lnfecingreso.setDate(self.emp[13])
				
			self.lncuenta.setText(self.emp[14])
			
			if self.emp[16] == None:
				self.lnfecegreso.setDate(QDate(1, 1, 1900))
			else:
				self.lnfecegreso.setDate(self.emp[16])
			self.lnfoto.setText(self.emp[17])
			self.idcargo=self.emp[18]
			self.tipemp=self.emp[19]
			self.iddpto=self.emp[20]
			self.idtiponom=self.emp[21]
			self.idbanco=self.emp[22]					
			
			self.fillcombos()
			self.fillgrid()
			self.lblfoto.setPixmap(QPixmap('fotos/'+self.lnfoto.text()))
		else:			
			self.botonera.btnModificar.setEnabled(False)
			self.botonera.btnEliminar.setEnabled(False)
			self.clear_fields()
		
		
	def clear_fields(self):
		self.lncodigo.setText('')
		self.lnsexo.setText('')
		self.lnnombres.setText('')
		self.lnapellidos.setText('')		
		self.lncedula.setText('')
		self.lnrif.setText('')
		self.lntlfhab.setText('')
		self.lntlfcel.setText('')
		#self.lnfecnac.date=''
		self.txtdir1.setPlainText('')
		self.txtdir2.setPlainText('')
		self.lnemail.setText('')
		#self.lnfecingresodate=''
		self.lncuenta.setText('')
		#self.lnfecegreso.date=''
		self.lnsmen.setText('')
		self.lnssem.setText('')
		self.lnsdiario.setText('')
		#self.lnfecsueldo.date=''
		self.lnfoto.setText('')
		
		
	def fillgrid(self):				
		self.sqldet = 'select id, fecha_desde, mensual,semanal,diario from cf_sueldo where cf_empleado_id ='+str(self.empid)
		self.model.setQuery(self.sqldet);		
		for i in range(0, len(self.headersdet)):
			self.model.setHeaderData(i, Qt.Horizontal, self.headersdet[i])
			self.model.setHeaderData(i, Qt.Horizontal, self.headersdet[i])
		self.tableView.setModel(self.model)
		self.tableView.setColumnHidden(0, True)
		self.tableView.setColumnWidth ( 1, 70 )
		self.tableView.setColumnWidth ( 2, 100 )
		self.tableView.setColumnWidth ( 3, 100 )
		self.tableView.show()


	def fillcombos(self):
		#debo vaciarlos antes a todos
		self.cmbbanco.clear()
		self.cmbcargo.clear()
		self.cmbdpto.clear()
		self.cmbtipemp.clear()
		self.cmbtipnom.clear()
		
		#tipo de empleado query
		self.query=QSqlQuery("select * from cf_empleado_tipo",self.db.db);
		while self.query.next():
		# se agrega el string  a mostrar y luego el id de la tabla	como un qvariant
			ids = self.query.value(0).toInt()[0] 				
			self.cmbtipemp.addItem(self.query.value(1).toString() , QVariant(ids))

		#departamento
		self.query=QSqlQuery("select * from cf_departamento",self.db.db);
		while self.query.next():
				# se agrega el srting y luego el id de la tabla
			ids = self.query.value(0).toInt()[0] 				
			self.cmbdpto.addItem(self.query.value(1).toString() , QVariant(ids))
				
		#cargo
		self.query=QSqlQuery("select * from cf_cargo",self.db.db);
		while self.query.next():
				# se agrega el srting y luego el id de la tabla
			ids = self.query.value(0).toInt()[0] 				
			self.cmbcargo.addItem(self.query.value(1).toString() , QVariant(ids))

		#tiponomina
		self.query=QSqlQuery("select * from cf_nomina_tipo",self.db.db);
		while self.query.next():
				# se agrega el srting y luego el id de la tabla
			ids = self.query.value(0).toInt()[0] 				
			self.cmbtipnom.addItem(self.query.value(1).toString() , QVariant(ids))

		#banco
		self.query=QSqlQuery("select * from cf_banco",self.db.db);
		while self.query.next():
				# se agrega el srting y luego el id de la tabla
			ids = self.query.value(0).toInt()[0] 				
			self.cmbbanco.addItem(self.query.value(1).toString() , QVariant(ids))

		# asi seteo el combo en el valor actual traido de la tabla
		#tipoempleado
		for cur in range(0, self.cmbtipemp.count()):						
			if  self.cmbtipemp.itemData(cur).toInt()[0] == self.tipemp:				
				self.cmbtipemp.setCurrentIndex(cur)
		
		#departamento
		for cur in range(0, self.cmbdpto.count()):						
			if  self.cmbdpto.itemData(cur).toInt()[0] == self.iddpto:				
				self.cmbdpto.setCurrentIndex(cur)
			
		#cargo
		for cur in range(0, self.cmbcargo.count()):						
			if  self.cmbcargo.itemData(cur).toInt()[0] == self.idcargo:				
				self.cmbcargo.setCurrentIndex(cur)

		#tiponomina
		for cur in range(0, self.cmbtipnom.count()):						
			if  self.cmbtipnom.itemData(cur).toInt()[0] == self.idtiponom:
				self.cmbtipnom.setCurrentIndex(cur)

		#banco
		for cur in range(0, self.cmbbanco.count()):						
			if  self.cmbbanco.itemData(cur).toInt()[0] == self.idbanco:				
				self.cmbbanco.setCurrentIndex(cur)

	@pyqtSignature("")
	def on_actionNuevo_triggered(self):
		self.isadding=True
		self.clear_fields()		
		self.frame_2.setEnabled(True)
		self.frame_3.setEnabled(True)
		self.frame_4.setEnabled(True)
		self.frame_5.setEnabled(True)
		
    
	@pyqtSignature("")
	def on_actionModificar_triggered(self):
		self.isediting=True		
		self.frame_2.setEnabled(True)
		self.frame_3.setEnabled(True)
		self.frame_4.setEnabled(True)
		self.frame_5.setEnabled(True)
		
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
			datos=['cf_empleado', self.empid]
			rs=self.datos.delete_record(datos)
			if rs:
				self.mensaje='Registro eliminado'
				self.msgBox.setText(self.mensaje)
				self.msgBox.exec_()
				if self.datos.check_havedata('cf_empleado'):
					self.fill_data()
				else:
					self.clear_fields()
					
	@pyqtSignature("")
	def on_actionGuardar_triggered(self):
		"""
        Slot documentation goes here.
        """
		self.idcargo=self.cmbcargo.itemData(self.cmbcargo.currentIndex()).toInt()[0]
		self.tipemp=self.cmbtipemp.itemData(self.cmbtipemp.currentIndex()).toInt()[0]
		self.iddpto=self.cmbdpto.itemData(self.cmbdpto.currentIndex()).toInt()[0]		
		self.idtiponom=self.cmbtipnom.itemData(self.cmbtipnom.currentIndex()).toInt()[0]		
		self.idbanco=self.cmbbanco.itemData(self.cmbbanco.currentIndex()).toInt()[0]		
				
		
#		if self.lnfecingreso.date().toPyDate().isoformat()=='1900-01-01':
#			self.lnfecingreso.date='0000-00-00'
#		else: 
#			self.lnfecingreso.date=self.lnfecingreso.date().toPyDate().isoformat()
#
#		if self.lnfecegreso.date().toPyDate().isoformat()=='1900-01-01':
#			self.lnfecegreso.date='0000-00-00'
#		else: 
#			self.lnfecegreso.date=self.lnfecegreso.date().toPyDate().isoformat()


		if self.isadding:
			datos=[ 
			self.lncodigo.text(), 
			self.lnsexo.text(), 
			self.lnnombres.text(), 
			self.lnapellidos.text(), 
			self.lncedula.text(), 
			self.lnrif.text(), 
			self.lntlfhab.text(), 
			self.lntlfcel.text(), 
			self.lnfecnac.date().toPyDate().isoformat(), 
			self.txtdir1.toPlainText(), 
			self.txtdir2.toPlainText(), 
			self.lnemail.text(), 
			self.lnfecingreso.date().toPyDate().isoformat(), 
			self.lncuenta.text(), 
			datetime.date.today().isoformat() , 
			self.lnfecegreso.date().toPyDate().isoformat(), 
			self.lnfoto.text(), 
			self.idcargo, 
			self.tipemp, 
			self.iddpto, 
			self.idtiponom, 
			self.idbanco
			]	
			self.lastid=self.datos.save_empleado(datos)
			if self.lastid>0:
				self.mensaje='Datos salvados con exito'			
			else:
				self.mensaje='No se pudo insertar'			
			
		elif self.isediting:
			datos=[
			self.lncodigo.text(), 
			self.lnsexo.text(), 
			self.lnnombres.text(), 
			self.lnapellidos.text(), 	
			self.lncedula.text(), 
			self.lnrif.text(), 
			self.lntlfhab.text(), 
			self.lntlfcel.text(), 
			self.lnfecnac.date().toPyDate().isoformat(), 
			self.txtdir1.toPlainText(), 
			self.txtdir2.toPlainText(), 
			self.lnemail.text(), 
			self.lnfecingreso.date().toPyDate().isoformat(), 
			self.lncuenta.text(), 
			self.lnfecegreso.date().toPyDate().isoformat(), 
			self.lnfoto.text(), 
			self.idcargo, 
			self.tipemp, 
			self.iddpto, 
			self.idtiponom, 
			self.idbanco, 
			self.empid]
			self.result=self.datos.update_empleado(datos)			
			self.lastid=self.empid
			if self.result > 0:
				self.mensaje='Datos actualizados con exito'
			else:
				self.mensaje='No se actualizo'
				
		#print 'last id'+str(self.lastid)
		
		self.frame_2.setEnabled(False)
		self.frame_3.setEnabled(False)
		self.frame_4.setEnabled(False)
		self.frame_5.setEnabled(False)
		
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
			if len(self.lnsmen.text()) > 0 and len(self.lnfecsueldo.date().toString()) > 0:
				datos=[self.lnfecsueldo.date().toPyDate().isoformat(),self.lnsmen.text(),self.lnssem.text(), self.lnsdiario.text(),   self.empid]
				self.lastdetid=self.datos.save_sueldo(datos)
				if self.lastdetid > 0:	
					self.lnsmen.setText('')
					#self.lnfecsueldo.setText('')
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
	def on_pushDel_released(self):
		"""
		Slot documentation goes here.
		"""
		if self.isediting:			
			datos=['cf_sueldo', self.idtodelete[0]]
			rs=self.datos.delete_record(datos)
			self.fillgrid()
		else:
			self.mensaje='Funcion disponible solo en modo edicion'
			self.msgBox.setText(self.mensaje)
			self.msgBox.exec_();
		self.pushDel.setEnabled(False)
		
	@pyqtSignature("QModelIndex")
	def on_tableView_clicked(self, index):
		"""
		Slot documentation goes here.
		"""
		self.idtodelete =  self.model.record(index.row()).value('id').toInt()
		self.pushDel.setEnabled(True)

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
			
	@pyqtSignature("int")
	def on_cmbtipemp_currentIndexChanged(self, index):
		pass
		#print 'indice ->'+str(index)
		#print 'indice->'+str(self.cmbtipemp.itemData(index, 1).toInt()[0])
		#print 'indice->'+str(self.cmbtipemp.itemData(index).toInt()[0])		

	@pyqtSignature("QString")
	def on_lnsmen_textChanged(self, p0):		
		trans='{:10,.2f}'.format(self.lnsmen.text().toDouble()[0]/4)
		trans2='{:10,.2f}'.format(self.lnsmen.text().toDouble()[0]/30)		
		self.lnssem.setText(str(trans))                                                     		
		self.lnsdiario.setText(str(trans2))
	
	@pyqtSignature("")
	def on_btnfoto_released(self):
		fileName = QFileDialog.getOpenFileName(self, "Seleccione Archivo", "/home", "Solo Imagenes (*.png *.jpg *.bmp)")
		
		fileonly=os.path.basename(str(fileName))
		self.lnfoto.setText(fileonly)
		shutil.copy(str(fileName), 'fotos/'+fileonly)
		self.lblfoto.setPixmap(QPixmap('fotos/'+fileonly))
		

import recurso_rc			
			
if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	ui = Empleados()
	ui.show()	
	sys.exit(app.exec_())
	ui.db.close()	
	ok = self.db.close()		
