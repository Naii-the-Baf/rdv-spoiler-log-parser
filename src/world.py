import re
from collections import defaultdict

import game
from gui.notification_dialog import NotificationDialog
from PySide6 import QtWidgets
import re


class World:
    def __init__(self, world: dict):
        self.game_id: str = world["game"]
        self.game: game.Game = game.NotSupportedGame()
        self.items: dict = world["locations"]
        self.starting: list[str] = ["Unknown"]
        self.starting_location: tuple[str, str] = "Unknown"

        if "starting_equipment" in world:
            self.starting = world["starting_equipment"]["pickups"]

        if "starting_location" in world:
            self.starting_location = re.split(r"\/", world["starting_location"])[:2]

        match self.game_id:
            case "am2r":
                self.game = game.AM2R()
            case "fusion":
                self.game = game.Fusion()
            case "dread":
                self.game = game.Dread()
            case "prime1":
                self.game = game.Prime1()
            case "prime2":
                self.game = game.Prime2()
            case "prime3":
                self.game = game.Prime3()
            case _:
                pass

    def get_item_locations(
        self, parent: QtWidgets.QWidget
    ) -> tuple[dict, dict, list[str]]:
        # If we're on a not supported game, handle things extra
        if isinstance(self.game, game.NotSupportedGame):
            return self.get_non_supported_game_locations()

        major_items = defaultdict(list)  # Name: [(region, room, reference)]
        minor_items = defaultdict(list)
        victory = defaultdict(list)
        invalid: list = []

        for region, locations in self.items.items():
            for location, pickup in locations.items():
                room, descriptor = re.split(r"\/Pickup \d?", location)
                if room is None or descriptor is None:
                    raise ValueError(f"Error while reading spoiler: Invalid item location: {location} {pickup}")
                if pickup in self.game.minor_items:
                    # Minor
                    minor_items[pickup].append((region, room, descriptor))
                elif any(pickup in category for category in self.game.major_items):
                    # Major
                    major_items[pickup].append((region, room, descriptor))
                elif self.game.victory_key in pickup:
                    # Victory key
                    victory[pickup].append((region, room, descriptor))
                else:
                    # Add unknown, but valid items to minor items
                    minor_items[pickup].append((region, room, descriptor))
                    self.game.minor_items.append(pickup)
                    invalid.append(pickup)
                    print(f"Invalid pickup: {location} {pickup}")
        major_items.update(victory)
        self.game.major_items.append(victory)

        if len(invalid) > 0:
            message = "The following pickups were present in the spoiler file, but are not supported:<br>"
            for pickup in invalid:
                message = f"{message}{pickup}<br>"
            NotificationDialog.show(parent, "Error while importing", message)

        return (major_items, minor_items, self.starting)

    def get_non_supported_game_locations(self) -> tuple[dict, dict, list[str]]:
        # Treat everything as major
        major_items = defaultdict(list)
        for region, locations in self.items.items():
            for location, pickup in locations.items():
                room, ref_item = re.split(r"\/Pickup \d?", location)
                if room is None or ref_item is None:
                    raise ValueError(f"Error while reading spoiler: Invalid item location: {location} {pickup}")
                major_items[pickup].append((region, room, ref_item))

        return (major_items, {}, self.starting)
