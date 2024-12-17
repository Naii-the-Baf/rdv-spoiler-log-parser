from __future__ import annotations
import json
from world import World
from enum import Enum


class SpoilerFile:
    json: dict
    world_names: list | None

    def __init__(self):
        self.json = {}
        self.world_names = None

    def read(self, filename) -> SpoilerStatusEnum:
        try:
            with open(filename, "r") as file:
                self.json = json.load(file)
                file.close()
        except (json.JSONDecodeError, UnicodeDecodeError):
            return SpoilerStatusEnum.JSON_READ_ERROR
        except Exception:
            return SpoilerStatusEnum.FILE_READ_ERROR
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


class SpoilerStatusEnum(str, Enum):
    message: str

    def __new__(cls, title: str, message: str = "") -> SpoilerStatusEnum:
        obj = str.__new__(cls, title)
        obj._value_ = title

        obj.message = message
        return obj

    OK = (0, "")
    JSON_READ_ERROR = (1, "Invalid rdvgame")
    FILE_READ_ERROR = (2, "File could not be read")
