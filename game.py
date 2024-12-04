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
        
class Prime1(Game):
    def __init__(self):
        super().__init__()
        self.dock_connections = None
        self.has_hints = False
        self.has_regions = True
        self.major_items = [
            [
                "Power Beam",
                "Wave Beam",
                "Ice Beam",
                "Plasma Beam",
                "Charge Beam",
            ],[
                "Super Missile",
                "Wavebuster",
                "Ice Spreader",
                "Flamethrower",
                "Missile Launcher",
            ],[
                "Combat Visor",
                "Scan Visor",
                "Thermal Visor",
                "X-Ray Visor",
            ],[
                "Morph Ball",
                "Boost Ball",
                "Spider Ball",
                "Morph Ball Bomb",
                "Power Bomb",
            ],[
                "Varia Suit",
                "Gravity Suit",
                "Phazon Suit",
            ],[
                "Space Jump Boots",
                "Grapple Beam",
            ],[
                "Artifact of Truth",
                "Artifact of Strength",
                "Artifact of Elder",
                "Artifact of Wild",
                "Artifact of Lifegiver",
                "Artifact of Warrior",
                "Artifact of Chozo",
                "Artifact of Nature",
                "Artifact of Sun",
                "Artifact of World",
                "Artifact of Spirit",
                "Artifact of Newborn",
            ],
        ]
        self.minor_items = [
            "Energy Tank",
            "Missile Expansion",
            "Power Bomb Expansion",
            "Energy Transfer Module",
        ]
        self.nothing_item = "Energy Transfer Module"
        self.special_configurations = []
        self.victory_key = "Artifact of"

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
                "Violet Translator",
                "Amber Translator",
                "Emerald Translator",
                "Cobalt Translator",
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
                "Sky Temple Key 1",
                "Sky Temple Key 2",
                "Sky Temple Key 3",
                "Sky Temple Key 4",
                "Sky Temple Key 5",
                "Sky Temple Key 6",
                "Sky Temple Key 7",
                "Sky Temple Key 8",
                "Sky Temple Key 9",
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
            "Energy Transfer Module",
        ]
        self.nothing_item = "Energy Transfer Module"
        self.special_configurations = []
        self.victory_key = "Sky Temple Key"

class Prime3(Game):
    def __init__(self):
        super().__init__()
        self.dock_connections = None
        self.has_hints = False
        self.has_regions = True
        self.major_items = [
            [
                "Power Beam",
                "Plasma Beam",
                "Nova Beam",
                "Progressive Beam",
                "Charge Beam",
            ],[
                "Missile Launcher",
                "Ice Missile",
                "Seeker Missile",
                "Progressive Missile",
            ],[
                "Combat Visor",
                "Scan Visor",
                "Command Visor",
                "X-Ray Visor",
            ],[
                "Morph Ball",
                "Boost Ball",
                "Spider Ball",
                "Morph Ball Bombs",
            ],[
                "Hazard Shield",
                "Space Jump Boots",
                "Screw Attack",
            ],[
                "Hypermode",
                "Hyper Ball",
                "Hyper Missile",
                "Hyper Grapple",
            ],[
                "Grapple Lasso",
                "Grapple Swing",
                "Grapple Voltage",
            ],[
                "Ship Missile",
                "Ship Grapple",
            ],[
                "Energy Cell 1",
                "Energy Cell 2",
                "Energy Cell 3",
                "Energy Cell 4",
                "Energy Cell 5",
                "Energy Cell 6",
                "Energy Cell 7",
                "Energy Cell 8",
                "Energy Cell 9",
            ],
        ]
        self.minor_items = [
            "Energy Tank",
            "Missile Expansion",
            "Ship Missile Expansion",
            "Energy Transfer Module",
        ]
        self.nothing_item = "Energy Transfer Module"
        self.special_configurations = []
        self.victory_key = "Energy Cell"