import sys
from PySide6 import QtWidgets
from arg_parser import ArgParser
from spoiler_file import SpoilerFile
from gui.main import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
    
    #parser = ArgParser()
    #args = parser.GetArgs()

    #print(items['permalink'])
