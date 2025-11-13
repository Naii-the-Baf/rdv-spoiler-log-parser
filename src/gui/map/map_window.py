import json
import re
from collections import defaultdict
from pathlib import Path

from PySide6 import QtCore, QtGui, QtWidgets

from world import World


class MapWindow(QtWidgets.QMainWindow):
    scroll_area: QtWidgets.QScrollArea
    maps: dict[str, QtGui.QPixmap]

    def __init__(self):
        super().__init__()
        self.maps = dict()

        self.setWindowTitle("Map")

        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setGeometry(0, 0, 800, 800)
        self.scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setEnabled(True)
        self.setCentralWidget(self.scroll_area)

    def draw_pickup_to_map(self, map_name: str, pickup_image: QtGui.QPixmap, x: int, y: int) -> None:
        painter = QtGui.QPainter(self.maps[map_name])
        painter.drawPixmap(QtCore.QPoint(x, y), pickup_image)
        painter.end()

    def draw_map(self, map_key: str) -> None:
        image_label = QtWidgets.QLabel()
        image_label.setPixmap(self.maps[map_key])
        self.scroll_area.setWidget(image_label)

        map_size = self.maps[map_key].size()
        self.resize(map_size.width() + 10, map_size.height() + 10)

    def load_maps(self, world: World) -> None:
        game_assets_path = Path(f"assets/{world.game_id}")

        with game_assets_path.joinpath("locations.json").open(mode="r") as file:
            region_maps: dict = json.load(file)

        with game_assets_path.joinpath("pickups.json").open(mode="r") as file:
            pickup_paths: dict = json.load(file)

        # Preload all known pickups' images
        pickup_images: dict[str, QtGui.QPixmap] = dict()
        for pickup_name, pickup_file in pickup_paths.items():
            pickup_images[pickup_name] = QtGui.QPixmap(game_assets_path.joinpath(f"pickups/{pickup_file}"))

        # Set up items for faster iteration
        locations: defaultdict[str, dict[str, str]] = defaultdict(dict)
        for item in world.items:
            identifier = item["node_identifier"]
            region = identifier["region"]
            area = identifier["area"]
            node = re.search(r"\(.+\)", identifier["node"])[0]  # type: ignore
            locations[region][" ".join([area, node])] = item["pickup"]

        for map_name, region_map in region_maps.items():
            map_path = game_assets_path.joinpath(f"maps/{region_map['map']}")
            self.maps[map_name] = QtGui.QPixmap(map_path)

            for area_node, offset in region_map["locations"].items():
                pickup = locations[region_map["region"]][area_node]
                if pickup in pickup_images.keys():
                    print(f"Drawing {pickup} at {region_map['region']}/{area_node}")
                    self.draw_pickup_to_map(map_name, pickup_images[pickup], offset["x"], offset["y"])
                else:
                    print(f"Drawing Default at {region_map['region']}/{area_node}")
                    self.draw_pickup_to_map(map_name, pickup_images["Default"], offset["x"], offset["y"])

        self.draw_map(next(iter(self.maps.keys())))
