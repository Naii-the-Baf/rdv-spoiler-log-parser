from PySide6 import QtCore, QtWidgets
from world import World
from gui.notification_dialog import NotificationDialog
import gui.styles as styles


class GameLayout(QtWidgets.QWidget):
    game_style: styles.BaseStyle
    world: World
    layout_obj: QtWidgets.QGridLayout

    def __init__(self, world: World):
        super().__init__()
        self.game_style = styles.BaseStyle()
        self.world = world
        unsupported_game = False

        match self.world.game_id:
            case "fusion":
                self.game_style = styles.FusionStyle()
            case "dread":
                self.game_style = styles.DreadStyle()
            case "prime1":
                self.game_style = styles.Prime1Style()
            case "prime2":
                self.game_style = styles.Prime2Style()
            case "prime3":
                self.game_style = styles.Prime3Style()
            case _:
                unsupported_game = True

        try:
            item_locations = self.world.get_item_locations()
        except ValueError as e:
            NotificationDialog.show(self, "Error", str(e))
            return

        self.layout_obj = QtWidgets.QGridLayout(self)
        self.setLayout(self.layout_obj)

        self.layout_obj.setColumnStretch(0, 20)
        self.layout_obj.setColumnStretch(1, 30)
        self.layout_obj.setColumnStretch(2, 50)

        starting = ", ".join(item_locations[2])
        starting_label = QtWidgets.QLabel(f"Starting items: {starting}")
        starting_label.setWordWrap(True)
        self.layout_obj.addWidget(starting_label, 0, 0, 1, 3)

        row_pos = 1
        if unsupported_game:
            NotificationDialog.show(
                self, "Warning", f"Game {self.world.game_id} is not supported"
            )
            print(f"Game {self.world.game_id} is not supported")
            self.build_items_display(
                list(item_locations[0].keys()), item_locations[0], row_pos
            )

        for item_category in self.world.game.major_items:
            row_pos = self.build_items_display(
                item_category, item_locations[0], row_pos
            )

            separator = QtWidgets.QLabel("")
            self.layout_obj.addWidget(separator, row_pos, 0, 1, 3)
            row_pos += 1

        self.build_items_display(
            self.world.game.minor_items, item_locations[1], row_pos
        )

    def build_items_display(self, item_set: list, locations: dict, offset: int) -> int:
        for item in item_set:
            if len(locations[item]) == 0:
                continue

            text = QtWidgets.QLabel(item)
            text.setStyleSheet("border:1px solid black;")

            style = self.game_style
            if self.world.game.victory_key in item:
                text.setStyleSheet(
                    f"border:1px solid black;background:{style.victory_background};color:black;"
                )
            text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.layout_obj.addWidget(text, offset, 0, len(locations[item]), 1)

            for region, area, vanilla_item in locations[item]:
                region_label = QtWidgets.QLabel(region)
                region_label.setStyleSheet(
                    f"background:{style.background.get(region, style.fallback_background)};color:{style.foreground.get(region, style.fallback_foreground)};"
                )
                self.layout_obj.addWidget(region_label, offset, 1, 1, 1)
                area_label = QtWidgets.QLabel(" ".join([area, vanilla_item]))
                area_label.setStyleSheet(
                    f"background:{style.background.get(region, style.fallback_background)};color:{style.foreground.get(region, style.fallback_foreground)};"
                )
                self.layout_obj.addWidget(area_label, offset, 2, 1, 1)
                offset = offset + 1
        return offset
