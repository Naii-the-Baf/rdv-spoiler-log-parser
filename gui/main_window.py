from PySide6 import QtCore, QtWidgets, QtGui
from spoiler_file import SpoilerFile
from gui.game_layout import GameLayout

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, file = None):
        super().__init__()
        self.dark_mode = True
        self.text_size = 12
        
        self.setWindowTitle("Spoiler Log Parser")
        
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scrollArea")
        self.scroll_area.setEnabled(True)
        self.setCentralWidget(self.scroll_area)
        self.scroll_area.setStyleSheet("background:#333333;color:white;font-size:12px;")
        
        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        preferences_menu = menu.addMenu("Preferences")
        
        load_action = QtGui.QAction("Load", self)
        load_action.setStatusTip("Load an rdvgame file")
        load_action.triggered.connect(self.load_file_dialog)
        file_menu.addAction(load_action)
        
        dark_mode_action = QtGui.QAction("Dark Mode", self)
        dark_mode_action.setStatusTip("Enables or disables dark mode.")
        dark_mode_action.setCheckable(True)
        dark_mode_action.setChecked(True)
        dark_mode_action.triggered.connect(self.toggle_mode)
        preferences_menu.addAction(dark_mode_action)
        
        bigger_text_action = QtGui.QAction("Increase Text Size", self)
        bigger_text_action.setStatusTip("Makes the text bigger.")
        bigger_text_action.triggered.connect(self.increase_text_size)
        preferences_menu.addAction(bigger_text_action)
        
        smaller_text_action = QtGui.QAction("Decrease Text Size", self)
        smaller_text_action.setStatusTip("Makes the text smaller.")
        smaller_text_action.triggered.connect(self.decrease_text_size)
        preferences_menu.addAction(smaller_text_action)
        
        if file != None:
            self.load_file(file)
        
    def load_file_dialog(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Load file...", filter="Randovania Game (*.rdvgame)")
        if file[0] == '':
            return
        self.load_file(file[0])
        
    def load_file(self, file):
        spoiler = SpoilerFile()
        spoiler.read(file)
        seed_details = spoiler.get_seed_details()
        print(seed_details)
        
        if 'game_modifications' not in spoiler.json:
            self.show_race_spoiler_log()
            return
        
        worlds = spoiler.get_worlds()
        self.scroll_area.setWidget(GameLayout(worlds[0]))
        
    def toggle_mode(self):
        if self.dark_mode:
            self.set_light_mode()
            return
        self.set_dark_mode()
    
    def set_light_mode(self):
        self.scroll_area.setStyleSheet(self.scroll_area.styleSheet().replace("background:#333333;color:white;", "background:#DDDDDD;color:black;"))
        self.dark_mode = False
        
    def set_dark_mode(self):
        self.scroll_area.setStyleSheet(self.scroll_area.styleSheet().replace("background:#DDDDDD;color:black;", "background:#333333;color:white;"))
        self.dark_mode = True
        
    def increase_text_size(self):
        if self.text_size <= 10:
            return
        self.scroll_area.setStyleSheet(self.scroll_area.styleSheet().replace("font-size:"+str(self.text_size)+"px;", "font-size:"+str(self.text_size + 1)+"px;"))
        self.text_size += 1
        
    def decrease_text_size(self):
        if self.text_size <= 24:
            return
        self.scroll_area.setStyleSheet(self.scroll_area.styleSheet().replace("font-size:"+str(self.text_size)+"px;", "font-size:"+str(self.text_size - 1)+"px;"))
        self.text_size -= 1

    def show_race_spoiler_dialog(self):
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