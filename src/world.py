from collections import defaultdict
import game
import re


class World:
    def __init__(self, world: dict):
        self.game_id: str = world["game"]
        self.game: game.Game = game.NotSupportedGame()
        self.items: dict = world["locations"]
        self.starting: list[str] = ["Unknown"]

        if "starting_equipment" in world:
            self.starting = world["starting_equipment"]["pickups"]

        match self.game_id:
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

        for region, locations in self.items.items():
            for location, pickup in locations.items():
                room, ref_item = re.split(r"\/Pickup \d?", location)
                if room is None or ref_item is None:
                    raise ValueError(
                        f"Error while reading spoiler: Invalid item location: {location} {pickup}"
                    )
                if pickup in self.game.minor_items:
                    # Minor
                    minor_items[pickup].append((region, room, ref_item))
                elif any(pickup in category for category in self.game.major_items):
                    # Major
                    major_items[pickup].append((region, room, ref_item))
                else:
                    raise ValueError(
                        f"Error while reading spoiler: Invalid pickup: {location} {pickup}"
                    )
        return (major_items, minor_items, self.starting)

    def get_non_supported_game_locations(self) -> tuple[dict, dict, list[str]]:
        # Treat everything as major
        major_items = defaultdict(list)
        for region, locations in self.items.items():
            for location, pickup in locations.items():
                room, ref_item = re.split(r"\/Pickup \d?", location)
                if room is None or ref_item is None:
                    raise ValueError(
                        f"Error while reading spoiler: Invalid item location: {location} {pickup}"
                    )
                major_items[pickup].append((region, room, ref_item))

        return (major_items, {}, self.starting)
