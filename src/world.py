import re
from collections import defaultdict

import game
from gui.notification_dialog import NotificationDialog


class World:
    def __init__(self, world: dict):
        self.game_id: str = world["game"]
        self.game: game.Game = game.NotSupportedGame()
        self.items: list[dict] = world["locations"]
        self.starting: list[str] = ["Unknown"]
        self.starting_location: tuple[str, str] = "Unknown"

        if "starting_equipment" in world:
            # print(world["starting_equipment"])
            try:
                # At some point, this changed and now there's two places where our starting items can be
                self.starting = world["starting_equipment"]["items"]
            except KeyError:
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

    def get_item_locations(self) -> tuple[dict, dict, list[str]]:
        # If we're on a not supported game, handle things extra
        if isinstance(self.game, game.NotSupportedGame):
            return self.get_non_supported_game_locations()

        major_items = defaultdict(list)  # Name: [(region, room, reference)]
        minor_items = defaultdict(list)
        victory = defaultdict(list)
        invalid: list = []

        for item in self.items:
            identifier = item["node_identifier"]
            # index = item["index"]
            pickup = item["pickup"]
            # owner = item["owner"]

            region = identifier["region"]
            area = identifier["area"]
            node = identifier["node"]

            if area is None or node is None:
                raise ValueError(f"Error while reading spoiler: Invalid item location: {area}/{node} {pickup}")
            if pickup in self.game.minor_items:
                # Minor
                minor_items[pickup].append((region, area, node))
            elif any(pickup in category for category in self.game.major_items):
                # Major
                major_items[pickup].append((region, area, node))
            elif self.game.victory_key in pickup:
                # Victory key
                victory[pickup].append((region, area, node))
            else:
                # Add unknown, but valid items to minor items
                minor_items[pickup].append((region, area, node))
                self.game.minor_items.append(pickup)
                invalid.append(pickup)
                print(f"Invalid pickup: {area}/{node} {pickup}")
        major_items.update(victory)
        self.game.major_items.append(victory)

        if len(invalid) > 0:
            message = "The following pickups were present in the spoiler file, but are not supported:<br>"
            for pickup in invalid:
                message = f"{message}{pickup}<br>"
            NotificationDialog.show("Error while importing", message)

        return (major_items, minor_items, self.starting)

    def get_non_supported_game_locations(self) -> tuple[dict, dict, list[str]]:
        # Treat everything as major
        major_items = defaultdict(list)
        for item in self.items:
            identifier = item["node_identifier"]
            # index = item["index"]
            pickup = item["pickup"]
            # owner = item["owner"]

            region = identifier["region"]
            area = identifier["area"]
            node = identifier["node"]

            if area is None or node is None:
                raise ValueError(f"Error while reading spoiler: Invalid item location: {area}/{node} {pickup}")
            major_items[pickup].append((region, area, node))

        return (major_items, {}, self.starting)
