from PySide6 import QtCore, QtWidgets, QtGui
from world import World
import game
#TODO: Import layouts as a module
from gui.layouts.base_layout import BaseLayout
from gui.layouts.prime1_style import Prime1Style
from gui.layouts.prime2_style import Prime2Style
from gui.layouts.prime3_style import Prime3Style
from gui.layouts.fusion_style import FusionStyle

class GameLayout(QtWidgets.QWidget):
    def __init__(self, world: World):
        super().__init__()
        self.game_style: BaseLayout = BaseLayout()
        self.world: World = world
        unsupported_game = False

        match self.world.game_id:
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
            print(f"game {self.world.game_id} is not supported")
        try:
            item_locations = self.world.get_item_locations()
        except ValueError as e:
            self.dialog_invalid_game(str(e))
            return
        
        self.layout: QtWidgets.QGridLayout = QtWidgets.QGridLayout(self)
        self.layout.setColumnStretch(0, 20)
        self.layout.setColumnStretch(1, 30)
        self.layout.setColumnStretch(2, 50)
        row_pos = 0
        
        for item_category in self.world.game.major_items:
            row_pos = self.build_items_display(item_category, item_locations[0], row_pos)
            
            separator = QtWidgets.QLabel("")
            self.layout.addWidget(separator, row_pos, 0, 1, 3)
            row_pos += 1
            
        self.build_items_display(self.world.game.minor_items, item_locations[1], row_pos)
    
    def build_items_display(self,
                            item_set: list,
                            locations: dict,
                            offset: int) -> int:
        for item in item_set:
            if len(locations[item]) == 0:
                continue
            
            text = QtWidgets.QLabel(item)
            text.setStyleSheet("border:1px solid black;")

            style = self.game_style
            if self.world.game.victory_key in item:
                text.setStyleSheet(f"border:1px solid black;background:{style.victory_background};color:black;")
            text.setAlignment(QtCore.Qt.AlignCenter)
            self.layout.addWidget(text, offset, 0, len(locations[item]), 1)

            for region, area, vanilla_item in locations[item]:
                region_label = QtWidgets.QLabel(region)
                region_label.setStyleSheet(f"background:{style.background.get(region, style.fallback_background)};color:{style.foreground.get(region, style.fallback_foreground)};")
                self.layout.addWidget(region_label, offset, 1, 1, 1)
                area_label = QtWidgets.QLabel(" ".join([area, vanilla_item]))
                area_label.setStyleSheet(f"background:{style.background.get(region, style.fallback_background)};color:{style.foreground.get(region, style.fallback_foreground)};")
                self.layout.addWidget(area_label, offset, 2, 1, 1)
                offset = offset + 1
        return offset

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