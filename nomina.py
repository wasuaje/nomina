from PyQt4 import QtCore, QtGui
from principal import Principal


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = Principal()
    ui.show()
    sys.exit(app.exec_())
