class BaseStyle:
    background: dict[str, str]
    foreground: dict[str, str]
    fallback_background: str
    fallback_foreground: str
    victory_background: str

    def __init__(self):
        self.background = {}
        self.foreground = {}
        self.fallback_background = "black"
        self.fallback_foreground = "white"
        self.victory_background = "#0ce561"


class AM2RStyle(BaseStyle):
    def __init__(self):
        super().__init__()

        self.background = {
            "Distribution Center": "#9fc5e8",
            "GFS Thoth": "#f9944a",
            "Golden Temple": "#ffe599",
            "Hydro Station": "#b6d7a8",
            "Industrial Complex": "#b4a7d6",
            "Main Caves": "#b05900",
            "The Depths": "#38761d",
            "The Tower": "#dd7e6b",
        }
        self.foreground = {
            "Distribution Center": "black",
            "GFS Thoth": "black",
            "Golden Temple": "black",
            "Hydro Station": "black",
            "Industrial Complex": "black",
            "Main Caves": "white",
            "The Depths": "white",
            "The Tower": "black",
        }

        self.victory_background = "#0ce561"


class FusionStyle(BaseStyle):
    def __init__(self):
        super().__init__()

        self.background = {
            "Main Deck": "#b7b7b7",
            "Sector 1 (SRX)": "#fae99a",
            "Sector 2 (TRO)": "#b7dba8",
            "Sector 3 (PYR)": "#d77b6e",
            "Sector 4 (AQA)": "#aabef4",
            "Sector 5 (ARC)": "#d2e1f3",
            "Sector 6 (NOC)": "#b5a2d6",
        }

        self.foreground = {
            "Main Deck": "black",
            "Sector 1 (SRX)": "black",
            "Sector 2 (TRO)": "black",
            "Sector 3 (PYR)": "black",
            "Sector 4 (AQA)": "black",
            "Sector 5 (ARC)": "black",
            "Sector 6 (NOC)": "black",
        }

        self.victory_background = "#0ce561"


class DreadStyle(BaseStyle):
    def __init__(self):
        super().__init__()

        self.background = {
            "Artaria": "#ffe599",
            "Burenia": "#72bddd",
            "Cataris": "#dd7e6b",
            "Dairon": "#eb9aca",
            "Elun": "#b4a7d6",
            "Ferenia": "#6d9eeb",
            "Ghavoran": "#b6d7a8",
            "Hanubia": "#a88160",
        }

        self.foreground = {
            "Artaria": "black",
            "Burenia": "black",
            "Cataris": "black",
            "Dairon": "black",
            "Elun": "black",
            "Ferenia": "black",
            "Ghavoran": "black",
            "Hanubia": "black",
        }

        self.victory_background = "#0ce561"


class Prime1Style(BaseStyle):
    def __init__(self):
        super().__init__()

        self.background = {
            "Chozo Ruins": "#d8c4af",
            "Magmoor Caverns": "#dd7e6b",
            "Phazon Mines": "#b4a7d6",
            "Phendrana Drifts": "#bfbfbf",
            "Tallon Overworld": "#9fbc93",
        }

        self.foreground = {
            "Chozo Ruins": "black",
            "Magmoor Caverns": "black",
            "Phazon Mines": "black",
            "Phendrana Drifts": "black",
            "Tallon Overworld": "black",
        }

        self.victory_background = "#17baba"


class Prime2Style(BaseStyle):
    def __init__(self):
        super().__init__()

        self.background = {
            "Agon Wastes": "#d8cead",
            "Dark Agon Wastes": "#783f04",
            "Dark Torvus Bog": "#38761d",
            "Ing Hive": "#1155cc",
            "Great Temple": "#d5a6bd",
            "Sanctuary Fortress": "#8eafce",
            "Sky Temple Grounds": "#351c75",
            "Temple Grounds": "#b4a7d6",
            "Torvus Bog": "#9fbc93",
        }

        self.foreground = {
            "Agon Wastes": "black",
            "Dark Agon Wastes": "white",
            "Dark Torvus Bog": "white",
            "Ing Hive": "white",
            "Great Temple": "black",
            "Sanctuary Fortress": "black",
            "Sky Temple Grounds": "white",
            "Temple Grounds": "black",
            "Torvus Bog": "black",
        }

        self.victory_background = "#93c47d"


class Prime3Style(BaseStyle):
    def __init__(self):
        super().__init__()

        self.background = {
            "Bryyo - Fire": "#f9944a",
            "Bryyo - Ice": "#cfe2f3",
            "Bryyo - Reptilicus": "#9fbc93",
            "Bryyo - Seed": "#3c78d8",
            "G.F.S. Olympus": "#8eafce",
            "G.F.S. Valhalla": "#d5a6bd",
            "Norion": "#bfbfbf",
            "Pirate Homeworld - Command": "#dd7e6b",
            "Pirate Homeworld - Mines": "#4dc923",
            "Pirate Homeworld - Research": "#cc4125",
            "Pirate Homeworld - Seed": "#3c78d8",
            "SkyTown, Elysia - Main": "#d8c4af",
            "SkyTown, Elysia - Pod": "#f9cb9c",
            "SkyTown, Elysia - Seed": "#3c78d8",
        }

        self.foreground = {
            "Bryyo - Fire": "black",
            "Bryyo - Ice": "black",
            "Bryyo - Reptilicus": "black",
            "Bryyo - Seed": "white",
            "G.F.S. Olympus": "black",
            "G.F.S. Valhalla": "black",
            "Norion": "black",
            "Pirate Homeworld - Command": "black",
            "Pirate Homeworld - Mines": "black",
            "Pirate Homeworld - Research": "white",
            "Pirate Homeworld - Seed": "white",
            "SkyTown, Elysia - Main": "black",
            "SkyTown, Elysia - Pod": "black",
            "SkyTown, Elysia - Seed": "white",
        }

        self.victory_background = "#0ce561"
