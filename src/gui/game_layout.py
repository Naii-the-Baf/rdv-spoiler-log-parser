from PySide6 import QtCore, QtWidgets

from gui.notification_dialog import NotificationDialog
from gui.styles import get_style_for_game
from gui.styles.base_style import BaseStyle, NotSupportedStyle
from world import World


class GameLayout(QtWidgets.QWidget):
    game_style: BaseStyle
    world: World
    layout_obj: QtWidgets.QGridLayout

    def __init__(self, world: World):
        super().__init__()
        self.world = world
        self.game_style = get_style_for_game(self.world.game_id)
        unsupported_game = isinstance(self.game_style, NotSupportedStyle)

        try:
            item_locations = self.world.get_item_locations()
        except ValueError as e:
            NotificationDialog.show("Error", str(e))
            return

        self.layout_obj = QtWidgets.QGridLayout(self)
        self.setLayout(self.layout_obj)

        self.layout_obj.setColumnStretch(0, 20)
        self.layout_obj.setColumnStretch(1, 30)
        self.layout_obj.setColumnStretch(2, 50)

        starting = ", ".join(world.get_starting_items())
        starting_label = QtWidgets.QLabel(f"Starting items: {starting}")
        starting_label.setWordWrap(True)
        self.layout_obj.addWidget(starting_label, 0, 0, 1, 3)

        self.layout_obj.addWidget(QtWidgets.QLabel("Starting location:"), 1, 0, 1, 1)
        starting_region, starting_room = world.starting_location
        starting_location_label = QtWidgets.QLabel(f"{starting_region}/{starting_room}")
        starting_location_label.setStyleSheet(
            (
                f"background:{self.game_style.background.get(starting_region, self.game_style.fallback_background)};"
                f"color:{self.game_style.foreground.get(starting_region, self.game_style.fallback_foreground)};"
            )
        )
        starting_location_label.setWordWrap(True)
        self.layout_obj.addWidget(starting_location_label, 1, 1, 1, 2)

        separator = QtWidgets.QLabel("")
        self.layout_obj.addWidget(separator, 2, 0, 1, 3)

        row_pos = 3
        if unsupported_game:
            NotificationDialog.show("Warning", f"Game {self.world.game_id} is not supported")
            print(f"Game {self.world.game_id} is not supported")
            self.build_items_display(list(item_locations["major"].keys()), item_locations["major"], row_pos)
            return

        for category_name, category_items in self.world.game.major_items.items():
            name_label = QtWidgets.QLabel(category_name)
            name_label.setStyleSheet(
                name_label.styleSheet().join("border-bottom-width:1px;border-bottom-style:solid;border-radius:0px;")
            )
            self.layout_obj.addWidget(name_label, row_pos, 0, 1, 3)
            row_pos += 1

            row_pos = self.build_items_display(category_items, item_locations["major"], row_pos)

            separator = QtWidgets.QLabel("")
            self.layout_obj.addWidget(separator, row_pos, 0, 1, 3)
            row_pos += 1

        name_label = QtWidgets.QLabel(self.world.game.victory_key)
        name_label.setStyleSheet(
            name_label.styleSheet().join("border-bottom-width:1px;border-bottom-style:solid;border-radius:0px;")
        )
        self.layout_obj.addWidget(name_label, row_pos, 0, 1, 4)
        row_pos += 1
        row_pos = self.build_items_display(list(item_locations["victory"].keys()), item_locations["victory"], row_pos)
        separator = QtWidgets.QLabel("")
        self.layout_obj.addWidget(separator, row_pos, 0, 1, 4)
        row_pos += 1

        row_pos = self.build_items_display(self.world.game.minor_items, item_locations["minor"], row_pos)
        row_pos = self.build_items_display(list(item_locations["unknown"].keys()), item_locations["unknown"], row_pos)

    def build_items_display(self, item_set: list, locations: dict, offset: int) -> int:
        for item in item_set:
            if len(locations[item]) == 0:
                continue

            text = QtWidgets.QLabel(item)
            text.setStyleSheet("border:1px solid black;")

            style = self.game_style
            if self.world.game.victory_key in item:
                text.setStyleSheet(f"border:1px solid black;background:{style.victory_background};color:black;")
            text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.layout_obj.addWidget(text, offset, 0, len(locations[item]), 1)

            for region, area, vanilla_item in locations[item]:
                region_label = QtWidgets.QLabel(region)
                region_label.setStyleSheet(
                    (
                        f"background:{style.background.get(region, style.fallback_background)};"
                        f"color:{style.foreground.get(region, style.fallback_foreground)};"
                    )
                )
                self.layout_obj.addWidget(region_label, offset, 1, 1, 1)
                area_label = QtWidgets.QLabel(" ".join([area, vanilla_item]))
                area_label.setStyleSheet(
                    (
                        f"background:{style.background.get(region, style.fallback_background)};"
                        f"color:{style.foreground.get(region, style.fallback_foreground)};"
                    )
                )
                self.layout_obj.addWidget(area_label, offset, 2, 1, 1)
                offset = offset + 1
        return offset
