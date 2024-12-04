from PySide6 import QtCore, QtWidgets, QtGui
import game
#TODO: Import layouts as a module
from gui.layouts.prime1_style import Prime1Style
from gui.layouts.prime2_style import Prime2Style
from gui.layouts.prime3_style import Prime3Style

class GameLayout(QtWidgets.QWidget):
    def __init__(self, world):
        super().__init__()
        self.game_style = None
        self.game = None

        match world.game_id:
            case 'prime1':
                self.game_style = Prime1Style()
                self.game = game.Prime1()
            case 'prime2':
                self.game_style = Prime2Style()
                self.game = game.Prime2()
            case 'prime3':
                self.game_style = Prime3Style()
                self.game = game.Prime3()
            case _:
                self.game_style = None

        item_locations = world.GetItemLocations()
        
        self.layout : QtWidgets.QGridLayout = QtWidgets.QGridLayout(self)
        self.layout.setColumnStretch(0, 20)
        self.layout.setColumnStretch(1, 30)
        self.layout.setColumnStretch(2, 50)
        row_pos = 0
        category = 0
        
        for item_category in item_locations:
            for item, locations in item_category.items():
                if len(locations) == 0:
                    continue
                
                while (category < len(self.game.major_items)) and (item not in self.game.major_items[category]):
                    category += 1
                    separator = QtWidgets.QLabel("")
                    self.layout.addWidget(separator, row_pos, 0, 1, 3)
                    row_pos += 1
                
                text = QtWidgets.QLabel(item)
                text.setStyleSheet("border:1px solid black;")
                if world.game.victory_key in item:
                    text.setStyleSheet("border:1px solid black;background:" + self.game_style.victory_background + ";color:black;")
                text.setAlignment(QtCore.Qt.AlignCenter)
                self.layout.addWidget(text, row_pos, 0, len(locations), 1)
                for location in locations:
                    text = QtWidgets.QLabel(location[0])
                    text.setStyleSheet("background:" + self.game_style.background[location[0]] + ";color:" + self.game_style.foreground[location[0]] + ";")
                    self.layout.addWidget(text, row_pos, 1, 1, 1)
                    text = QtWidgets.QLabel(" ".join([location[1], location[2]]))
                    text.setStyleSheet("background:" + self.game_style.background[location[0]] + ";color:" + self.game_style.foreground[location[0]] + ";")
                    self.layout.addWidget(text, row_pos, 2, 1, 1)
                    row_pos += 1
