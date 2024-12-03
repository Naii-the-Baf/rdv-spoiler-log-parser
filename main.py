import sys
from PySide6 import QtWidgets
from gui.main import MainWindow
from arg_parser import ArgParser

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    
    parser = ArgParser()
    args = parser.GetArgs()

    widget = MainWindow(args.file)
    widget.resize(600, 600)
    widget.show()

    sys.exit(app.exec())
