import sys
import signal
from PySide6 import QtCore, QtWidgets, QtGui
from gui.main_window import MainWindow
from arg_parser import ArgParser

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    
    parser = ArgParser()
    args = parser.get_args()
    
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    signal.signal(signal.SIGTERM, signal.SIG_DFL)
    
    widget = MainWindow(args.file)
    widget.resize(600, 600)
    widget.show()

    sys.exit(app.exec())
