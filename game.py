class Game:
    def __init__(self):
        self.dock_connections = None
        self.has_hints = False
        self.has_regions = False
        self.major_items = []
        self.minor_items = []
        self.nothing_item = "Energy Transfer Module"
        self.special_configurations = []
        self.victory_key = None
        
class Prime2(Game):
    def __init__(self):
        super().__init__()
        self.dock_connections = None
        self.has_hints = True
        self.has_regions = True
        self.major_items = [
            [
                "Power Beam",
                "Dark Beam",
                "Light Beam",
                "Annihilator Beam",
                "Charge Beam",
            ],[
                "Super Missile",
                "Darkburst",
                "Super Missile",
                "Darkburst",
                "Sunburst",
                "Sonic Boom",
                "Missile Launcher",
                "Seeker Launcher",
            ],[
                "Combat Visor",
                "Scan Visor",
                "Dark Visor",
                "Echo Visor",
            ],[
                "Morph Ball",
                "Boost Ball",
                "Spider Ball",
                "Morph Ball Bomb",
                "Power Bomb",
            ],[
                "Dark Suit",
                "Light Suit",
                "Progressive Suit",
            ],[
                "Space Jump Boots",
                "Gravity Boost",
                "Grapple Beam",
                "Screw Attack",
                "Progressive Grapple",
            ],[
                "Dark Agon Key 1",
                "Dark Agon Key 2",
                "Dark Agon Key 3",
                "Dark Torvus Key 1",
                "Dark Torvus Key 2",
                "Dark Torvus Key 3",
                "Ing Hive Key 1",
                "Ing Hive Key 2",
                "Ing Hive Key 3",
            ],[
                "Violet Translator",
                "Amber Translator",
                "Emerald Translator",
                "Cobalt Translator",
            ],[
                "Unlimited Missiles",
                "Unlimited Beam Ammo",
                "Double Damage",
                "Cannon Ball",
            ],
        ]
        self.minor_items = [
            "Energy Tank",
            "Missile Expansion",
            "Power Bomb Expansion",
            "Beam Ammo Expansion",
            "Dark Ammo Expansion",
            "Light Ammo Expansion",
        ]
        self.nothing_item = "Energy Transfer Module"
        self.special_configurations = []
        self.victory_key = "Sky Temple Key"
