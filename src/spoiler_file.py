from __future__ import annotations

import json
from enum import Enum
from pathlib import Path

from randovania.layout.layout_description import InvalidLayoutDescription, LayoutDescription  # type: ignore

from world import World


class SpoilerFile:
    layout: LayoutDescription
    world_names: list | None

    def __init__(self):
        self.world_names = None

    def read(self, filename) -> SpoilerStatusEnum:
        try:
            self.layout = LayoutDescription.from_file(Path(filename))
            # print(self.layout._serialized_patches)
        except InvalidLayoutDescription:
            return SpoilerStatusEnum.INVALID_LAYOUT
        except (json.JSONDecodeError, UnicodeDecodeError):
            return SpoilerStatusEnum.JSON_READ_ERROR
        except Exception as e:
            print(e)
            return SpoilerStatusEnum.FILE_READ_ERROR
        return SpoilerStatusEnum.OK

    def get_seed_details(self) -> dict:
        details = dict()
        details["permalink"] = self.layout.permalink.as_base64_str
        details["hash"] = self.layout.shareable_hash
        details["word_hash"] = self.layout.shareable_word_hash
        details["has_spoiler"] = self.layout.has_spoiler
        return details

    def set_world_names(self, names=None):
        if names is None:
            self.world_names = list()
            for i in range(len(self.layout.all_presets)):
                self.world_names.append(f"Player {i}")
            return
        self.world_names = names

    def get_worlds(self) -> list[World]:
        if self.world_names is None:
            self.set_world_names()

        worlds = list()
        for world in self.layout._serialized_patches:
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
    INVALID_LAYOUT = (3, "The rdvgame file does not contain a spoiler; did you try loading a race file?")
