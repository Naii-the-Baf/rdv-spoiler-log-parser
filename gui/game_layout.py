from PySide6 import QtCore, QtWidgets, QtGui
import game
#TODO: Import layouts as a module
from gui.layouts.base_layout import BaseLayout
from gui.layouts.prime1_style import Prime1Style
from gui.layouts.prime2_style import Prime2Style
from gui.layouts.prime3_style import Prime3Style
from gui.layouts.fusion_style import FusionStyle

class GameLayout(QtWidgets.QWidget):
    def __init__(self, world):
        super().__init__()
        self.game_style = BaseLayout()
        unsupported_game = False

        match world.game_id:
            case 'prime1':
                self.game_style = Prime1Style()
            case 'prime2':
                self.game_style = Prime2Style()
            case 'prime3':
                self.game_style = Prime3Style()
            case 'fusion':
                self.game_style = FusionStyle()
            case _:
                unsupported_game = True

        if unsupported_game:
            # TODO: show a dialog or a label somewhere
            print(f"game {world.game_id} is not supported")
        try:
            item_locations = world.get_item_locations()
        except ValueError as e:
            self.dialog_invalid_game(str(e))
            return
        
        self.layout: QtWidgets.QGridLayout = QtWidgets.QGridLayout(self)
        self.layout.setColumnStretch(0, 20)
        self.layout.setColumnStretch(1, 30)
        self.layout.setColumnStretch(2, 50)
        row_pos = 0
        category = 0
        
        for item_category in item_locations:
            for item, locations in item_category.items():
                if len(locations) == 0:
                    continue

                while (category < len(world.game.major_items)) and (item not in world.game.major_items[category]):
                    category += 1
                    separator = QtWidgets.QLabel("")
                    self.layout.addWidget(separator, row_pos, 0, 1, 3)
                    row_pos += 1
                
                text = QtWidgets.QLabel(item)
                text.setStyleSheet("border:1px solid black;")

                style = self.game_style
                if world.game.victory_key in item:
                    text.setStyleSheet("border:1px solid black;background:" + style.victory_background + ";color:black;")
                text.setAlignment(QtCore.Qt.AlignCenter)
                self.layout.addWidget(text, row_pos, 0, len(locations), 1)

                for region, area, vanilla_item in locations:
                    region_label = QtWidgets.QLabel(region)
                    region_label.setStyleSheet("background:" + style.background.get(region, style.fallback_background) + ";color:" + style.foreground.get(region, style.fallback_foreground) + ";")
                    self.layout.addWidget(region_label, row_pos, 1, 1, 1)
                    area_label = QtWidgets.QLabel(" ".join([area, vanilla_item]))
                    area_label.setStyleSheet("background:" + style.background.get(region, style.fallback_background) + ";color:" + style.foreground.get(region, style.fallback_foreground) + ";")
                    self.layout.addWidget(area_label, row_pos, 2, 1, 1)
                    row_pos += 1

    def dialog_invalid_game(self, message):
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("Error")
        dialog_layout = QtWidgets.QVBoxLayout()
        label_message = QtWidgets.QLabel("Invalid rdvgame")
        dialog_layout.addWidget(label_message)
        label_error = QtWidgets.QLabel(message)
        dialog_layout.addWidget(label_error)
        dialog.setLayout(dialog_layout)
        dialog.exec()