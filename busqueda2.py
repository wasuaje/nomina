# -*- coding: utf-8 -*-

"""
Module implementing Busqueda.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature,  Qt, SIGNAL
from PyQt4 import QtGui
from PyQt4.QtSql import *

from ui.Ui_busqueda import Ui_Dialog
from  dbdata import *

class Busqueda(QDialog, Ui_Dialog):
	"""
	Class documentation goes here.
	"""
	
		
	def __init__(self, parent = None):
		"""
		Constructor
		"""
		QDialog.__init__(self, parent)
		self.setupUi(self)
	
		self.campos=[]
		self.tabla=''
		self.headers=[]	
		self.sql=''			
		self.db=None
	
	def fillgrid(self):				
		
		#self.db=QDbdata()
		#ok = self.db.open()
		self.model = QSqlQueryModel(self)
		self.model.setQuery(self.sql, self.db.db);		
		for i in range(0, len(self.headers)):
			self.model.setHeaderData(i, Qt.Horizontal, self.headers[i])
			self.model.setHeaderData(i, Qt.Horizontal, self.headers[i])
		self.tableView.setModel(self.model)
		self.tableView.setColumnHidden(0, True)
		self.tableView.setColumnWidth ( 1, 165 )
		self.tableView.setColumnWidth ( 2, 185 )
		self.tableView.show()
		#ok = self.db.close()		
	
		
	@pyqtSignature("")
	def on_buttonBox_accepted(self):
		"""
		Slot documentation goes here.
		"""
		self.close()
    
	@pyqtSignature("")
	def on_buttonBox_rejected(self):
		"""
		Slot documentation goes here.
		"""
		self.close()

	@pyqtSignature("QString")
	def on_lineEdit_textChanged(self, p0):
		"""
		Slot documentation goes here.
		"""
		self.sql3=self.sql
		#raise NotImplementedError
		if len(p0) > 2:
			#funciona para dos campos de busqueda
			#self.sql= 'select '+ ','.join(self.campos) + ' from '+self.tabla 	+ " where "+self.campos[1]+" like '%"+p0+ "%' or "+self.campos[2]+" like '%"+p0+"%'"
			#lambda para hacerlo sin importar el nro de campos
			self.sql= 'select '+ ','.join(self.campos) + ' from '+self.tabla 	+ " where "+' or '.join(map(lambda x: x + " like '%"+str(p0)+"%'", self.campos))
		if len(p0) < 3:
			self.sql= 'select '+ ','.join(self.campos) + ' from '+self.tabla 	
		self.fillgrid()
		#print self.sql
		
    
	@pyqtSignature("")
	def on_lineEdit_returnPressed(self):
		"""
		Slot documentation goes here.
		"""
		# TODO: not implemented yet
		raise NotImplementedError
    
	@pyqtSignature("QModelIndex")
	def on_tableView_clicked(self, index):
		"""
		Slot documentation goes here.
		"""
		# TODO: not implemented yet
		#raise NotImplementedError
		id =  self.model.record(index.row()).value('id').toInt()
		self.emit(SIGNAL("tableView_clicked"),  id[0])
		self.close()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = Busqueda()
    ui.show()
    sys.exit(app.exec_())
