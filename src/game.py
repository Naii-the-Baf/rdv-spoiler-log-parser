class Game:
    dock_connections: list
    major_items: list
    minor_items: list
    nothing_item: str
    special_configurations: list
    victory_key: str

    def __init__(self):
        self.dock_connections = None
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
            [  # Missiles
                "Missile Launcher",
                "Super Missile Launcher",
            ],
            [  # Morph Ball
                "Morph Ball",
                "Bombs",
                "Spider Ball",
                "Spring Ball",
                "Power Bomb Launcher",
            ],
            [  # Movement
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
        self.victory_key = "Metroid DNA"


class Fusion(Game):
    def __init__(self):
        super().__init__()
        self.dock_connections = None
        self.major_items = [
            [  # Beams
                "Charge Beam",
                "Wide Beam",
                "Plasma Beam",
                "Wave Beam",
                "Ice Beam",
            ],
            [  # Missile systems
                "Missile Launcher Data",
                "Super Missile Data",
                "Ice Missile Data",
                "Diffusion Missile Data",
            ],
            [  # Morph upgrades
                "Morph Ball",
                "Morph Ball Bomb Data",
                "Power Bomb Data",
            ],
            [  # Suits
                "Varia Suit",
                "Gravity Suit",
            ],
            [  # Misc
                "Hi-Jump",
                "Space Jump",
                "Speed Booster",
                "Screw Attack",
            ],
            [  # Keycards
                "Level 1 Keycard",
                "Level 2 Keycard",
                "Level 3 Keycard",
                "Level 4 Keycard",
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
        self.major_items = [
            [  # Charge Beam
                "Charge Beam",
                "Diffusion Beam",
                "Progressive Charge Beam",
            ],
            [  # Beams
                "Wide Beam",
                "Plasma Beam",
                "Wave Beam",
                "Progressive Beam",
                "Grapple Beam",
            ],
            [  # Morph upgrades
                "Morph Ball",
                "Bomb",
                "Cross Bomb",
                "Progressive Bomb",
                "Power Bomb",
            ],
            [  # Movement systems
                "Slide",
                "Spider Magnet",
                "Speed Booster",
                "Spin Boost",
                "Space Jump",
                "Progressive Spin",
                "Screw Attack",
            ],
            [  # Missile systems
                "Missile Launcher",
                "Super Missile",
                "Ice Missile",
                "Progressive Missile",
                "Storm Missile",
            ],
            [  # Aeion upgrades
                "Phantom Cloak",
                "Flash Shift",
                "Pulse Radar",
            ],
            [  # Suits
                "Varia Suit",
                "Gravity Suit",
                "Progressive Suit",
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
        self.major_items = [
            [  # Beams
                "Power Beam",
                "Wave Beam",
                "Ice Beam",
                "Plasma Beam",
                "Charge Beam",
            ],
            [  # Missiles + Beam combos
                "Super Missile",
                "Wavebuster",
                "Ice Spreader",
                "Flamethrower",
                "Missile Launcher",
            ],
            [  # Visors
                "Combat Visor",
                "Scan Visor",
                "Thermal Visor",
                "X-Ray Visor",
            ],
            [  # Morph upgrades
                "Morph Ball",
                "Boost Ball",
                "Spider Ball",
                "Morph Ball Bomb",
                "Power Bomb",
            ],
            [  # Suits
                "Varia Suit",
                "Gravity Suit",
                "Phazon Suit",
            ],
            [  # Movement systems
                "Space Jump Boots",
                "Grapple Beam",
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
        self.major_items = [
            [  # Beams
                "Power Beam",
                "Dark Beam",
                "Light Beam",
                "Annihilator Beam",
                "Charge Beam",
                "Unlimited Beam Ammo",
            ],
            [  # Missile systems
                "Missile Launcher",
                "Seeker Launcher",
                "Unlimited Missiles",
            ],
            [  # Beam combos
                "Super Missile",
                "Darkburst",
                "Sunburst",
                "Sonic Boom",
            ],
            [  # Visors
                "Combat Visor",
                "Scan Visor",
                "Dark Visor",
                "Echo Visor",
            ],
            [  # Morph upgrades
                "Morph Ball",
                "Boost Ball",
                "Spider Ball",
                "Morph Ball Bomb",
                "Power Bomb",
                "Cannon Ball",
            ],
            [  # Suits
                "Dark Suit",
                "Light Suit",
                "Progressive Suit",
                "Double Damage",
            ],
            [  # Movement systems
                "Space Jump Boots",
                "Gravity Boost",
                "Grapple Beam",
                "Screw Attack",
                "Progressive Grapple",
            ],
            [  # Translators
                "Violet Translator",
                "Amber Translator",
                "Emerald Translator",
                "Cobalt Translator",
            ],
            [  # Temple keys
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
        self.major_items = [
            [  # Beams
                "Power Beam",
                "Plasma Beam",
                "Nova Beam",
                "Progressive Beam",
                "Charge Beam",
            ],
            [  # Missile systems
                "Missile Launcher",
                "Ice Missile",
                "Seeker Missile",
                "Progressive Missile",
            ],
            [  # Visors
                "Combat Visor",
                "Scan Visor",
                "Command Visor",
                "X-Ray Visor",
            ],
            [  # Morph upgrades
                "Morph Ball",
                "Boost Ball",
                "Spider Ball",
                "Morph Ball Bombs",
            ],
            [  # Suits
                "Hazard Shield",
            ],
            [  # Movement systems
                "Space Jump Boots",
                "Screw Attack",
            ],
            [  # Hypermode upgrades
                "Hypermode",
                "Hyper Ball",
                "Hyper Missile",
                "Hyper Grapple",
            ],
            [  # Grapple upgrades
                "Grapple Lasso",
                "Grapple Swing",
                "Grapple Voltage",
            ],
            [  # Ship upgrades
                "Ship Missile",
                "Ship Grapple",
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
