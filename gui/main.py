from PySide6 import QtCore, QtWidgets, QtGui
import random
from spoiler_file import SpoilerFile
from arg_parser import ArgParser

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, file = None):
        super().__init__()
        
        toolbar = QtWidgets.QToolBar()
        toolbar.setAllowedAreas(QtCore.Qt.ToolBarArea.TopToolBarArea)
        toolbar.setFloatable(False)
        self.addToolBar(toolbar)
        
        self.setCentralWidget(MyWidget())
        
        button_action = QtGui.QAction("Load", self)
        button_action.setStatusTip("")
        button_action.triggered.connect(self.LoadFileDialog)
        
        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        file_menu.addAction(button_action)
        
        if file != None:
            self.LoadFile(file)
        
    def LoadFileDialog(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Load file...", filter="Randovania Game (*.rdvgame)")
        if file[0] == '':
            return
        self.LoadFile(file[0])
        
    def LoadFile(self, file):
        spoiler = SpoilerFile()
        spoiler.Read(file)
        seed_details = spoiler.GetSeedDetails()
        print(seed_details)

        
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["This", "is", "a", "test"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))
