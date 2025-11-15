import platform

from PySide6 import QtCore, QtGui, QtWidgets

from gui.game_layout import GameLayout
from gui.map import is_game_map_supported
from gui.map.map_window import MapWindow
from gui.notification_dialog import NotificationDialog
from settings import Settings
from spoiler_file import SpoilerFile, SpoilerStatusEnum
from world import World


class MainWindow(QtWidgets.QMainWindow):
    settings: Settings
    dark_mode: bool
    text_size: int
    map_window: MapWindow | None
    scroll_area: QtWidgets.QScrollArea
    current_world: World
    is_spoiler_loaded: bool

    def __init__(self, file: str | None = None):
        super().__init__()

        self.settings = Settings()
        self.dark_mode = self.settings.get_option("dark_mode")  # type: ignore
        self.text_size = self.settings.get_option("text_size")  # type: ignore

        # Validate text size in case it was modified externally
        if self.text_size < 10 or self.text_size > 24:
            self.text_size = 12
            self.settings.write_option("text_size", 12)

        self.map_window = None
        self.is_spoiler_loaded = False

        self.setWindowTitle("Spoiler Log Parser")

        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scrollArea")
        self.scroll_area.setEnabled(True)
        self.setCentralWidget(self.scroll_area)
        self.setStyleSheet(f"background:#333333;color:white;font-size:{self.text_size}px;")

        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        preferences_menu = menu.addMenu("Preferences")
        map_menu = menu.addMenu("Map")

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

        map_action = QtGui.QAction("Open Map", self)
        map_action.setStatusTip("Open a map with item locations.")
        map_action.triggered.connect(self.open_map_window)
        map_menu.addAction(map_action)

        about_action = QtGui.QAction("About", self)
        about_action.triggered.connect(self.about_dialog)
        menu.addAction(about_action)

        if not self.dark_mode:
            self.set_light_mode()

        if file is not None:
            self.load_file(file)

    def load_file_dialog(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("Randovania Game (*.rdvgame)")
        if file_dialog.exec() == QtWidgets.QDialog.DialogCode.Rejected:
            return
        files = file_dialog.selectedFiles()
        if len(files) == 0:
            return
        self.load_file(files[0])

    def load_file(self, file: str):
        spoiler = SpoilerFile()
        r = spoiler.read(file)
        if r != SpoilerStatusEnum.OK:
            NotificationDialog.show("Error", r.message)
            return
        seed_details = spoiler.get_seed_details()
        print(seed_details)

        worlds = spoiler.get_worlds()
        if len(worlds) > 1:
            NotificationDialog.show("Error", "Multiworlds are not supported.")
            return
        self.current_world = worlds[0]
        self.scroll_area.setWidget(GameLayout(self.current_world))
        self.is_spoiler_loaded = True

    def toggle_mode(self):
        if self.dark_mode:
            self.set_light_mode()
        else:
            self.set_dark_mode()
        self.settings.write_option("dark_mode", self.dark_mode)

        if self.map_window:
            self.map_window.setStyleSheet(self.styleSheet())

    def set_light_mode(self):
        self.setStyleSheet(
            self.styleSheet().replace("background:#333333;color:white;", "background:#DDDDDD;color:black;")
        )
        self.dark_mode = False

    def set_dark_mode(self):
        self.setStyleSheet(
            self.styleSheet().replace("background:#DDDDDD;color:black;", "background:#333333;color:white;")
        )
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

        button_values = QtWidgets.QDialogButtonBox.StandardButton.Apply
        button_box = QtWidgets.QDialogButtonBox(button_values)
        button_box.clicked.connect(lambda: self.change_text_size(text_edit_area.text(), dialog))
        dialog_layout.addWidget(button_box)

        dialog.setLayout(dialog_layout)
        dialog.exec()

    def change_text_size(self, value: int, parent: QtWidgets.QWidget):
        value = int(value)
        if value < 10 or value > 24:
            NotificationDialog.show(
                "Error",
                "Invalid text size; only allowed sizes are between 10px and 24px.",
            )
            if self.text_size < 10 or self.text_size > 24:
                self.text_size = 12
            return

        self.setStyleSheet(self.styleSheet().replace(f"font-size:{self.text_size}px;", f"font-size:{value}px;"))
        self.text_size = value
        print(f"Font size changed: {self.text_size}")
        self.settings.write_option("text_size", self.text_size)

        if self.map_window:
            self.map_window.setStyleSheet(self.styleSheet())

    def open_map_window(self):
        if not self.is_spoiler_loaded:
            NotificationDialog.show("Error", "You must load an rdvgame before opening a map.")
            return

        if not is_game_map_supported(self.current_world.game_id):
            NotificationDialog.show("Error", f"Maps not supported for game {self.current_world.game_id}")
            return

        self.map_window = MapWindow()
        self.map_window.resize(800, 800)
        self.map_window.setStyleSheet(self.styleSheet())
        self.map_window.show()
        self.map_window.load_maps(self.current_world)

    def about_dialog(self):
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("About")
        dialog.setStyleSheet(self.styleSheet())
        dialog_layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel("RDV Spoiler Log Parser v3.0.0", alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        dialog_layout.addWidget(label)

        label = QtWidgets.QLabel("randovania version 10.3.2 stable", alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        dialog_layout.addWidget(label)

        label = QtWidgets.QLabel(
            "Metroid Prime 2: Echoes maps sourced from <a href="
            '"https://metroid.retropixel.net/games/mprime2/maps.php">retropixel.net</a>, edited by loohhoo.',
            textFormat=QtCore.Qt.TextFormat.RichText,
            alignment=QtCore.Qt.AlignmentFlag.AlignCenter,
            openExternalLinks=True,
            textInteractionFlags=QtCore.Qt.TextInteractionFlag.TextBrowserInteraction,
        )
        dialog_layout.addWidget(label)

        label = QtWidgets.QLabel(
            "Metroid Prime 2: Echoes item icons sourced from <a href="
            '"https://www.spriters-resource.com/custom_edited/metroidcustoms/sheet/23198/">Spriter\'s Resource</a>.',
            textFormat=QtCore.Qt.TextFormat.RichText,
            alignment=QtCore.Qt.AlignmentFlag.AlignCenter,
            openExternalLinks=True,
            textInteractionFlags=QtCore.Qt.TextInteractionFlag.TextBrowserInteraction,
        )
        dialog_layout.addWidget(label)

        dialog.setLayout(dialog_layout)
        dialog.exec()

    # Override
    def dragEnterEvent(self, event: QtGui.QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.accept()
            return
        event.ignore()

    # Override
    def dragMoveEvent(self, event: QtGui.QDragMoveEvent):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.DropAction.CopyAction)
            event.accept()
            return
        event.ignore()

    # Override
    def dropEvent(self, event: QtGui.QDropEvent):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.DropAction.CopyAction)
            event.accept()

            # Remove the URI stuff to convert into a path
            path = event.mimeData().urls()[0].toString()
            # TODO: Make this cross-platform
            if platform.system() == "Windows":
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
