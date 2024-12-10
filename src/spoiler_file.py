import json
from world import World
from enum import Enum


class SpoilerFile:
    def __init__(self):
        self.json: dict = None
        self.world_names: list | None = None

    def read(self, filename) -> int:
        with open(filename, "r") as file:
            try:
                self.json = json.load(file)
            except (OSError, json.JSONDecodeError):
                return SpoilerStatusEnum.JSON_READ_ERROR
            finally:
                file.close()
        return SpoilerStatusEnum.OK

    def get_seed_details(self) -> dict:
        details = dict()
        details["permalink"] = self.json["info"]["permalink"]
        details["hash"] = self.json["info"]["hash"]
        details["word_hash"] = self.json["info"]["word_hash"]
        details["has_spoiler"] = self.json["info"]["has_spoiler"]
        return details

    def set_world_names(self, names=None):
        if names is None:
            self.world_names = list()
            for i in range(len(self.json["info"]["presets"])):
                self.world_names.append(f"Player {i}")
            return
        self.world_names = names

    def get_worlds(self) -> list[World]:
        if self.world_names is None:
            self.set_world_names()

        worlds = list()
        for world in self.json["game_modifications"]:
            worlds.append(World(world))
        return worlds


class SpoilerStatusEnum(Enum):
    OK = 0
    JSON_READ_ERROR = 1
