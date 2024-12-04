from PySide6 import QtCore, QtWidgets, QtGui
from spoiler_file import SpoilerFile
from gui.game_layout import GameLayout

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, file = None):
        super().__init__()
        
        self.setWindowTitle("Spoiler Log Parser")
        
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scrollArea")
        self.scroll_area.setEnabled(True)
        self.setCentralWidget(self.scroll_area)
        
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
        
        worlds = spoiler.GetWorlds()
        self.scroll_area.setWidget(GameLayout(worlds[0]))
