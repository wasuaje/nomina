# -*- coding: utf-8 -*-

"""
Module implementing Principal.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature

from ui.Ui_principal import Ui_MainWindow
from empresas import Empresas
from cargos import Cargos

class Principal(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_action_Empresa_triggered(self):
		"""
		Slot documentation goes here.
		"""
		self.empresa=Empresas(self)
		self.empresa.show()

    @pyqtSignature("")
    def on_actionCargos_triggered(self):
		"""
		Slot documentation goes here.
		"""
		self.cargos=Cargos(self)
		self.cargos.show()


    @pyqtSignature("")
    def on_action_Salir_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
