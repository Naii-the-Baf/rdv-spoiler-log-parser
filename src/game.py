class Game:
    dock_connections: list
    has_hints: bool
    major_items: list
    minor_items: list
    nothing_item: str
    special_configurations: list
    victory_key: str

    def __init__(self):
        self.dock_connections = None
        self.has_hints = False
        self.major_items = []
        self.minor_items = []
        self.nothing_item = "Energy Transfer Module"
        self.special_configurations = []
        self.victory_key = "A default victory key"


class NotSupportedGame(Game):
    def __init__(self):
        super().__init__()


class AM2R(Game):
    def __init__(self):
        self.dock_connections = None
        self.has_hints = False
        self.major_items = [
            [  # Beams
                "Power Beam",
                "Long Beam",
                "Charge Beam",
                "Spazer Beam",
                "Wave Beam",
                "Plasma Beam",
                "Ice Beam",
            ],
            [  # Missile systems
                "Missile Launcher",
                "Super Missile Launcher",
            ],
            [  # Morph upgrades
                "Morph Ball",
                "Bombs",
                "Spider Ball",
                "Spring Ball",
                "Power Bomb Launcher",
            ],
            [  # Misc
                "Power Grip",
                "Screw Attack",
                "Speed Booster",
                "Hi-Jump Boots",
                "Space Jump",
                "Progressive Jump",
                "Infinite Bomb Propulsion",
                "Walljump Boots",
            ],
            [  # Suits
                "Varia Suit",
                "Gravity Suit",
                "Progressive Suit",
            ],
            [  # Keys
                "Metroid DNA 1",
                "Metroid DNA 2",
                "Metroid DNA 3",
                "Metroid DNA 4",
                "Metroid DNA 5",
                "Metroid DNA 6",
                "Metroid DNA 7",
                "Metroid DNA 8",
                "Metroid DNA 9",
                "Metroid DNA 10",
                "Metroid DNA 11",
                "Metroid DNA 12",
                "Metroid DNA 13",
                "Metroid DNA 14",
                "Metroid DNA 15",
                "Metroid DNA 16",
                "Metroid DNA 17",
                "Metroid DNA 18",
                "Metroid DNA 19",
                "Metroid DNA 20",
                "Metroid DNA 21",
                "Metroid DNA 22",
                "Metroid DNA 23",
                "Metroid DNA 24",
                "Metroid DNA 25",
                "Metroid DNA 26",
                "Metroid DNA 27",
                "Metroid DNA 28",
                "Metroid DNA 29",
                "Metroid DNA 30",
                "Metroid DNA 31",
                "Metroid DNA 32",
                "Metroid DNA 33",
                "Metroid DNA 34",
                "Metroid DNA 35",
                "Metroid DNA 36",
                "Metroid DNA 37",
                "Metroid DNA 38",
                "Metroid DNA 39",
                "Metroid DNA 40",
                "Metroid DNA 41",
                "Metroid DNA 42",
                "Metroid DNA 43",
                "Metroid DNA 44",
                "Metroid DNA 45",
                "Metroid DNA 46",
            ],
        ]
        self.minor_items = [
            "Energy Tank",
            "Missile Tank",
            "Super Missile Tank",
            "Power Bomb Tank",
            "Small Health Drop",
            "Big Health Drop",
            "Missile Drop",
            "Super Missile Drop",
            "Power Bomb Drop",
            "Speed Booster Upgrade",
            "Flashlight",
            "Blindfold",
            "Energy Transfer Module",
        ]
        self.nothing_item = "Energy Transfer Module"
        self.special_configurations = []
        self.victory_key = "A default victory key"


class Fusion(Game):
    def __init__(self):
        super().__init__()
        self.dock_connections = None
        self.has_hints = False
        self.major_items = [
            [
                "Charge Beam",
                "Wide Beam",
                "Plasma Beam",
                "Wave Beam",
                "Ice Beam",
            ],
            [
                "Missile Launcher Data",
                "Super Missile Data",
                "Ice Missile Data",
                "Diffusion Missile Data",
            ],
            [
                "Morph Ball",
                "Morph Ball Bomb Data",
                "Power Bomb Data",
            ],
            [
                "Varia Suit",
                "Gravity Suit",
            ],
            [
                "Hi-Jump",
                "Space Jump",
                "Speed Booster",
                "Screw Attack",
            ],
            [
                "Level 1 Locks",
                "Level 2 Locks",
                "Level 3 Locks",
                "Level 4 Locks",
            ],
            [
                "Infant Metroid 1",
                "Infant Metroid 2",
                "Infant Metroid 3",
                "Infant Metroid 4",
                "Infant Metroid 5",
                "Infant Metroid 6",
                "Infant Metroid 7",
                "Infant Metroid 8",
                "Infant Metroid 9",
                "Infant Metroid 10",
                "Infant Metroid 11",
                "Infant Metroid 12",
                "Infant Metroid 13",
                "Infant Metroid 14",
                "Infant Metroid 15",
                "Infant Metroid 16",
                "Infant Metroid 17",
                "Infant Metroid 18",
                "Infant Metroid 19",
                "Infant Metroid 20",
            ],
        ]
        self.minor_items = [
            "Energy Tank",
            "Missile Tank",
            "Power Bomb Tank",
            "Energy Transfer Module",
        ]
        self.nothing_item = "Energy Transfer Module"
        self.special_configurations = []
        self.victory_key = "Infant Metroid"


class Dread(Game):
    def __init__(self):
        self.dock_connections = None
        self.has_hints = True
        self.major_items = [
            [
                "Charge Beam",
                "Diffusion Beam",
                "Progressive Charge Beam",
            ],
            [
                "Wide Beam",
                "Plasma Beam",
                "Wave Beam",
                "Progressive Beam",
                "Grapple Beam",
            ],
            [
                "Morph Ball",
                "Bomb",
                "Cross Bomb",
                "Progressive Bomb",
                "Power Bomb",
            ],
            [
                "Slide",
                "Spider Magnet",
                "Speed Booster",
                "Spin Boost",
                "Space Jump",
                "Progressive Spin",
                "Screw Attack",
            ],
            [
                "Missile Launcher",
                "Super Missile",
                "Ice Missile",
                "Progressive Missile",
                "Storm Missile",
            ],
            [
                "Phantom Cloak",
                "Flash Shift",
                "Pulse Radar",
            ],
            [
                "Varia Suit",
                "Gravity Suit",
                "Progressive Suit",
            ],
            [
                "Metroid DNA 1",
                "Metroid DNA 2",
                "Metroid DNA 3",
                "Metroid DNA 4",
                "Metroid DNA 5",
                "Metroid DNA 6",
                "Metroid DNA 7",
                "Metroid DNA 8",
                "Metroid DNA 9",
                "Metroid DNA 10",
                "Metroid DNA 11",
                "Metroid DNA 12",
            ],
        ]
        self.minor_items = [
            "Energy Part",
            "Energy Tank",
            "Missile Tank",
            "Missile+ Tank",
            "Power Bomb Tank",
            "Speed Booster Upgrade",
            "Flash Shift Upgrade",
            "Energy Transfer Module",
        ]
        self.nothing_item = "Energy Transfer Module"
        self.special_configurations = []
        self.victory_key = "Metroid DNA"


class Prime1(Game):
    def __init__(self):
        super().__init__()
        self.dock_connections = None
        self.has_hints = False
        self.major_items = [
            [
                "Power Beam",
                "Wave Beam",
                "Ice Beam",
                "Plasma Beam",
                "Charge Beam",
            ],
            [
                "Super Missile",
                "Wavebuster",
                "Ice Spreader",
                "Flamethrower",
                "Missile Launcher",
            ],
            [
                "Combat Visor",
                "Scan Visor",
                "Thermal Visor",
                "X-Ray Visor",
            ],
            [
                "Morph Ball",
                "Boost Ball",
                "Spider Ball",
                "Morph Ball Bomb",
                "Power Bomb",
            ],
            [
                "Varia Suit",
                "Gravity Suit",
                "Phazon Suit",
            ],
            [
                "Space Jump Boots",
                "Grapple Beam",
            ],
            [
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
        self.major_items = [
            [
                "Power Beam",
                "Dark Beam",
                "Light Beam",
                "Annihilator Beam",
                "Charge Beam",
            ],
            [
                "Super Missile",
                "Darkburst",
                "Sunburst",
                "Sonic Boom",
                "Missile Launcher",
                "Seeker Launcher",
            ],
            [
                "Combat Visor",
                "Scan Visor",
                "Dark Visor",
                "Echo Visor",
            ],
            [
                "Morph Ball",
                "Boost Ball",
                "Spider Ball",
                "Morph Ball Bomb",
                "Power Bomb",
            ],
            [
                "Dark Suit",
                "Light Suit",
                "Progressive Suit",
            ],
            [
                "Space Jump Boots",
                "Gravity Boost",
                "Grapple Beam",
                "Screw Attack",
                "Progressive Grapple",
            ],
            [
                "Violet Translator",
                "Amber Translator",
                "Emerald Translator",
                "Cobalt Translator",
            ],
            [
                "Dark Agon Key 1",
                "Dark Agon Key 2",
                "Dark Agon Key 3",
                "Dark Torvus Key 1",
                "Dark Torvus Key 2",
                "Dark Torvus Key 3",
                "Ing Hive Key 1",
                "Ing Hive Key 2",
                "Ing Hive Key 3",
            ],
            [
                "Sky Temple Key 1",
                "Sky Temple Key 2",
                "Sky Temple Key 3",
                "Sky Temple Key 4",
                "Sky Temple Key 5",
                "Sky Temple Key 6",
                "Sky Temple Key 7",
                "Sky Temple Key 8",
                "Sky Temple Key 9",
            ],
            [
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
        self.major_items = [
            [
                "Power Beam",
                "Plasma Beam",
                "Nova Beam",
                "Progressive Beam",
                "Charge Beam",
            ],
            [
                "Missile Launcher",
                "Ice Missile",
                "Seeker Missile",
                "Progressive Missile",
            ],
            [
                "Combat Visor",
                "Scan Visor",
                "Command Visor",
                "X-Ray Visor",
            ],
            [
                "Morph Ball",
                "Boost Ball",
                "Spider Ball",
                "Morph Ball Bombs",
            ],
            [
                "Hazard Shield",
                "Space Jump Boots",
                "Screw Attack",
            ],
            [
                "Hypermode",
                "Hyper Ball",
                "Hyper Missile",
                "Hyper Grapple",
            ],
            [
                "Grapple Lasso",
                "Grapple Swing",
                "Grapple Voltage",
            ],
            [
                "Ship Missile",
                "Ship Grapple",
            ],
            [
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
