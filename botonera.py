# -*- coding: utf-8 -*-

"""
Module implementing Botonera.
"""

from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature, SIGNAL

from ui.Ui_botonera import Ui_Form

class Botonera(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QWidget.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_btnNuevo_released(self):
		"""
		Slot documentation goes here.
		"""		
		self.btnNuevo.setEnabled(False)
		self.btnEliminar.setEnabled(False)
		self.btnModificar.setEnabled(False)
		self.btnSearch.setEnabled(False)
		self.btnPrint.setEnabled(False)
		self.btnSalir.setEnabled(True)
		self.btnGuardar.setEnabled(True)	
		
		self.emit(SIGNAL("btnNuevo_released"), ())
		
    @pyqtSignature("")
    def on_btnModificar_released(self):
		"""
		Slot documentation goes here.
		"""
		self.btnNuevo.setEnabled(False)
		self.btnEliminar.setEnabled(False)
		self.btnModificar.setEnabled(False)
		self.btnSearch.setEnabled(False)
		self.btnPrint.setEnabled(False)
		self.btnSalir.setEnabled(False)
		self.btnGuardar.setEnabled(True)	
		self.emit(SIGNAL("btnModificar_released"), ())
        
    
    @pyqtSignature("")
    def on_btnGuardar_released(self):
		"""
		Slot documentation goes here.
		"""
		self.btnNuevo.setEnabled(True)
		self.btnEliminar.setEnabled(True)
		self.btnModificar.setEnabled(True)
		self.btnSearch.setEnabled(True)
		self.btnPrint.setEnabled(True)
		self.btnSalir.setEnabled(True)
		self.btnGuardar.setEnabled(False)	
		self.emit(SIGNAL("btnGuardar_released"), ())
        
    
    @pyqtSignature("")
    def on_btnEliminar_released(self):
		"""
		Slot documentation goes here.
		"""
		self.emit(SIGNAL("btnEliminar_released"), ())
        

    @pyqtSignature("")
    def on_btnSearch_released(self):
		"""
		Slot documentation goes here.
		"""
		self.emit(SIGNAL("btnSearch_released"), ())
		
    @pyqtSignature("")
    def on_btnPrint_released(self):
		"""
		Slot documentation goes here.
		"""
		self.emit(SIGNAL("btnPrint_released"), ())
        

    @pyqtSignature("")
    def on_btnSalir_released(self):
		"""
		Slot documentation goes here.
		"""
		self.emit(SIGNAL("btnSalir_released"), ())
