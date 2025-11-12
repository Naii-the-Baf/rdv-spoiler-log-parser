from games.game import Game


class Prime2Game(Game):
    major_items = [
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
    minor_items = [
        "Energy Tank",
        "Missile Expansion",
        "Power Bomb Expansion",
        "Beam Ammo Expansion",
        "Dark Ammo Expansion",
        "Light Ammo Expansion",
        "Nothing",
    ]
    special_configurations = []
    victory_key = "Sky Temple Key"
