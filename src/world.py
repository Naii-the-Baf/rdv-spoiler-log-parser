import re
from collections import defaultdict

from games import get_game_by_id
from games.game import Game, NotSupportedGame
from gui.notification_dialog import NotificationDialog


class World:
    items: list[dict]

    def __init__(self, world: dict):
        self.game_id: str = world["game"]
        self.game: Game = NotSupportedGame()
        self.items = world["locations"]
        self.starting: list[str] = ["Unknown"]
        self.starting_location: tuple[str, str] = ("Unknown", "")

        if "starting_equipment" in world:
            # print(world["starting_equipment"])
            try:
                # At some point, this changed and now there's two places where our starting items can be
                self.starting = world["starting_equipment"]["items"]
            except KeyError:
                self.starting = world["starting_equipment"]["pickups"]

        if "starting_location" in world:
            self.starting_location = re.split(r"\/", world["starting_location"])[:2]  # type: ignore

        self.game = get_game_by_id(self.game_id)

    def get_item_locations(self) -> dict[str, dict]:
        # If we're on a not supported game, handle things extra
        if isinstance(self.game, NotSupportedGame):
            return self.get_non_supported_game_locations()

        major_items = defaultdict(list)  # Name: [(region, room, reference)]
        minor_items = defaultdict(list)
        unknown = defaultdict(list)
        victory = defaultdict(list)

        for item in self.items:
            identifier = item["node_identifier"]
            # index = item["index"]
            pickup = item["pickup"]
            # owner = item["owner"]

            region = identifier["region"]
            area = identifier["area"]
            node = re.search(r"\(.+\)", identifier["node"])[0]  # type: ignore

            if area is None or node is None:
                raise ValueError(f"Error while reading spoiler: Invalid item location: {area}/{node} {pickup}")
            if pickup in self.game.minor_items:
                # Minor
                minor_items[pickup].append((region, area, node))
            elif any(pickup in category for category in self.game.major_items.values()):
                # Major
                major_items[pickup].append((region, area, node))
            elif self.game.victory_key in pickup:
                # Victory key
                victory[pickup].append((region, area, node))
            else:
                # Add unknown, but valid items to unknown
                unknown[pickup].append((region, area, node))
                print(f"Invalid pickup: {area}/{node} {pickup}")
        major_items.update(victory)

        if len(unknown) > 0:
            message = "The following pickups were present in the spoiler file, but are not supported:<br>"
            for pickup in unknown.keys():
                message = f"{message}{pickup}<br>"
            NotificationDialog.show("Error while importing", message)

        return {
            "major": major_items,
            "victory": victory,
            "minor": minor_items,
            "unknown": unknown,
        }

    def get_non_supported_game_locations(self) -> dict[str, dict]:
        # Treat everything as major
        major_items = defaultdict(list)
        for item in self.items:
            identifier = item["node_identifier"]
            # index = item["index"]
            pickup = item["pickup"]
            # owner = item["owner"]

            region = identifier["region"]
            area = identifier["area"]
            node = re.search(r"\(.+\)", identifier["node"])[0]  # type: ignore

            if area is None or node is None:
                raise ValueError(f"Error while reading spoiler: Invalid item location: {area}/{node} {pickup}")
            major_items[pickup].append((region, area, node))

        return {
            "major": major_items,
            "victory": {},
            "minor": {},
        }

    def get_starting_items(self) -> list[str]:
        return self.starting
