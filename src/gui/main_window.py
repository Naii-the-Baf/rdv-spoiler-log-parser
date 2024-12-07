from PySide6 import QtCore, QtWidgets, QtGui
from spoiler_file import SpoilerFile, SpoilerStatusEnum
from gui.game_layout import GameLayout
from gui.notification_dialog import NotificationDialog
from settings import Settings
import platform

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, file: str | None = None):
        super().__init__()
        
        self.settings = Settings()
        self.options = self.settings.get_options()
        self.dark_mode: bool = self.options['dark_mode']
        self.text_size: int = self.options['text_size']
        
        # Validate text size in case it was modified externally
        if self.text_size < 10 or self.text_size > 24:
            self.text_size = 12
            self.settings.write_option('text_size', 12)
        
        self.setWindowTitle("Spoiler Log Parser")
        
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scrollArea")
        self.scroll_area.setEnabled(True)
        self.setCentralWidget(self.scroll_area)
        self.scroll_area.setStyleSheet(f"background:#333333;color:white;font-size:{self.text_size}px;")
        
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
        dark_mode_action.setChecked(self.dark_mode)
        dark_mode_action.triggered.connect(self.toggle_mode)
        preferences_menu.addAction(dark_mode_action)
        
        text_action = QtGui.QAction("Change Text Size", self)
        text_action.setStatusTip("Change the text size.")
        text_action.triggered.connect(self.change_text_size_dialog)
        preferences_menu.addAction(text_action)
        
        if not self.dark_mode:
            self.set_light_mode()
        
        if file is not None:
            self.load_file(file)
        
    def load_file_dialog(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("Randovania Game (*.rdvgame)")
        file_dialog.exec()
        files = file_dialog.selectedFiles()
        if len(files) == 0:
            return
        self.load_file(files[0])
        
    def load_file(self, file: str):
        spoiler = SpoilerFile()
        try:
            r = spoiler.read(file)
        except OSError:
            NotificationDialog.show(self, "Error", f"File \"{file}\" not be read")
            return
        if r != SpoilerStatusEnum.OK:
            NotificationDialog.show(self, "Error", "Invalid rdvgame")
            return
        seed_details = spoiler.get_seed_details()
        print(seed_details)
        
        if not seed_details['has_spoiler']:
            NotificationDialog.show(self, "Error", "The rdvgame file does not contain a spoiler; did you try loading a race file?")
            return
        
        worlds = spoiler.get_worlds()
        self.scroll_area.setWidget(GameLayout(worlds[0]))
        
    def toggle_mode(self):
        if self.dark_mode:
            self.set_light_mode()
        else:
            self.set_dark_mode()
        self.settings.write_option('dark_mode', self.dark_mode)
    
    def set_light_mode(self):
        self.scroll_area.setStyleSheet(self.scroll_area.styleSheet().replace("background:#333333;color:white;", "background:#DDDDDD;color:black;"))
        self.dark_mode = False
        
    def set_dark_mode(self):
        self.scroll_area.setStyleSheet(self.scroll_area.styleSheet().replace("background:#DDDDDD;color:black;", "background:#333333;color:white;"))
        self.dark_mode = True
        
    def change_text_size_dialog(self):
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("Text Size")
        dialog_layout = QtWidgets.QVBoxLayout()
        
        label = QtWidgets.QLabel("Insert a font size value between 10px and 24px.")
        dialog_layout.addWidget(label)
        
        text_edit_area = QtWidgets.QLineEdit(str(self.text_size), dialog)
        text_edit_area.setValidator(QtGui.QIntValidator(10, 24, text_edit_area))
        text_edit_area.returnPressed.connect(lambda: self.change_text_size(text_edit_area.text(), dialog))
        dialog_layout.addWidget(text_edit_area)
        
        button_values = QtWidgets.QDialogButtonBox.Apply
        button_box = QtWidgets.QDialogButtonBox(button_values)
        button_box.clicked.connect(lambda: self.change_text_size(text_edit_area.text(), dialog))
        dialog_layout.addWidget(button_box)
        
        dialog.setLayout(dialog_layout)
        dialog.exec()

    def change_text_size(self, value: int, parent: QtWidgets.QWidget):
        value = int(value)
        if value < 10 or value > 24:
            NotificationDialog.show(parent, "Error", "Invalid text size; only allowed sizes are between 10px and 24px.")
            if self.text_size < 10 or self.text_size > 24:
                self.text_size = 12
            return

        self.scroll_area.setStyleSheet(self.scroll_area.styleSheet().replace(
            f"font-size:{self.text_size}px;",
            f"font-size:{value}px;"))
        self.text_size = value
        print(f"Font size changed: {self.text_size}")
        self.settings.write_option('text_size', self.text_size)

    # Override
    def dragEnterEvent(self, event: QtGui.QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.accept()
            return
        event.ignore()
            
    # Override
    def dragMoveEvent(self, event: QtGui.QDragMoveEvent):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            return
        event.ignore()

    # Override
    def dropEvent(self, event: QtGui.QDropEvent):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            
            # Remove the URI stuff to convert into a path
            path = event.mimeData().urls()[0].toString()
            # TODO: Make this cross-platform
            if platform.system() == 'Windows':
                # Windows' routes are special
                path = path[8:]
            else:
                path = path[7:]
            self.load_file(path)
            return
        event.ignore()
    
    # Override
    def closeEvent(self, event: QtGui.QCloseEvent):
        self.settings.save_options_to_file()
        return super().closeEvent(event)
