from PySide6 import QtCore, QtWidgets, QtGui
from spoiler_file import SpoilerFile
from gui.game_layout import GameLayout

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, file = None):
        super().__init__()
        self.dark_mode = True
        self.bigger_text = False
        
        self.setWindowTitle("Spoiler Log Parser")
        
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scrollArea")
        self.scroll_area.setEnabled(True)
        self.setCentralWidget(self.scroll_area)
        self.scroll_area.setStyleSheet("background:#333333;color:white;")
        
        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        preferences_menu = menu.addMenu("Preferences")
        
        load_action = QtGui.QAction("Load", self)
        load_action.setStatusTip("Load an rdvgame file")
        load_action.triggered.connect(self.LoadFileDialog)
        file_menu.addAction(load_action)
        
        dark_mode_action = QtGui.QAction("Dark Mode", self)
        dark_mode_action.setStatusTip("Enables or disables dark mode.")
        dark_mode_action.setCheckable(True)
        dark_mode_action.setChecked(True)
        dark_mode_action.triggered.connect(self.ToggleMode)
        preferences_menu.addAction(dark_mode_action)
        
        bigger_text_action = QtGui.QAction("Bigger Text", self)
        bigger_text_action.setStatusTip("Makes the text bigger.")
        bigger_text_action.setCheckable(True)
        bigger_text_action.setChecked(False)
        bigger_text_action.triggered.connect(self.ToggleBiggerText)
        preferences_menu.addAction(bigger_text_action)
        
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
        
        if 'game_modifications' not in spoiler.json:
            self.ShowRaceSpoilerDialog()
            return
        
        worlds = spoiler.GetWorlds()
        self.scroll_area.setWidget(GameLayout(worlds[0]))
        
    def ToggleMode(self):
        if self.dark_mode:
            self.SetLightMode()
            return
        self.SetDarkMode()
    
    def SetLightMode(self):
        self.scroll_area.setStyleSheet(self.scroll_area.styleSheet().replace("background:#333333;color:white;", "background:#DDDDDD;color:black;"))
        self.dark_mode = False
        
    def SetDarkMode(self):
        self.scroll_area.setStyleSheet(self.scroll_area.styleSheet().replace("background:#DDDDDD;color:black;", "background:#333333;color:white;"))
        self.dark_mode = True
        
    def ToggleBiggerText(self):
        if self.bigger_text:
            self.scroll_area.setStyleSheet(self.scroll_area.styleSheet().replace("font-size:16px;", ""))
            self.bigger_text = False
            return
        self.scroll_area.setStyleSheet(self.scroll_area.styleSheet() + "font-size:16px;")
        self.bigger_text = True

    def ShowRaceSpoilerDialog(self):
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("Error")
        dialog_layout = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel("The rdvgame file does not contain a spoiler; did you try loading a race file?")
        dialog_layout.addWidget(message)
        
        button_values = QtWidgets.QDialogButtonBox.Ok
        button_box = QtWidgets.QDialogButtonBox(button_values)
        button_box.accepted.connect(dialog.accept)
        dialog_layout.addWidget(button_box)
        
        dialog.setLayout(dialog_layout)
        dialog.exec()