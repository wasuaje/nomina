# -*- coding: utf-8 -*-

"""
Module implementing Busqueda.
"""

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature, Qt
from PyQt4.QtSql import *

from Ui_busqueda import Ui_Form
from  dbdata import *

class Busqueda(QWidget, Ui_Form):
	"""
	Class documentation goes here.
	"""
	def __init__(self,  parent = None):
		"""
		Constructor
		"""
		QWidget.__init__(self, parent)
		self.setupUi(self)
		self.sql=''
		self.header=[]
		self.db=None
	
	def fillgrid(self):
		#self.db=QDbdata()
		#ok = self.db.open()
		self.model = QSqlQueryModel(self)
		self.model.setQuery(self.sql, slef.db.db);
		self.model.removeColumn(0)  # don't show the ID
		for i in range(0, len(self.headers)):
			self.model.setHeaderData(i, Qt.Horizontal, self.headers[i])
			self.model.setHeaderData(i, Qt.Horizontal, self.headers[i])
		self.tableView.setModel(self.model)
		#ok = self.db.close()		

   
	@pyqtSignature("QModelIndex")
	def on_tableView_clicked(self, index):
		"""
		Slot documentation goes here.
		"""
		# TODO: not implemented yet
		raise NotImplementedError
    
	@pyqtSignature("QModelIndex")
	def on_tableView_doubleClicked(self, index):
		"""
		Slot documentation goes here.
		"""
		# TODO: not implemented yet
		raise NotImplementedError
    
    
	@pyqtSignature("")
	def on_tableView_viewportEntered(self):
		"""
		Slot documentation goes here.
		"""
        # TODO: not implemented yet
        #raise NotImplementedError
    
	@pyqtSignature("QString")
	def on_lineEdit_textChanged(self, p0):
		"""
		Slot documentation goes here.
		"""
        # TODO: not implemented yet
        #raise NotImplementedError
    
	@pyqtSignature("QString")
	def on_lineEdit_textEdited(self, p0):
		"""
		Slot documentation goes here.
		"""
		# TODO: not implemented yet
        #raise NotImplementedError
    
	@pyqtSignature("")
	def on_lineEdit_returnPressed(self):
		"""
		Slot documentation goes here.
		"""
        # TODO: not implemented yet
        #raise NotImplementedError
    
	
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = Busqueda()
    ui.show()
    sys.exit(app.exec_())
	

