from games.game import Game


class DreadGame(Game):
    major_items = [
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
    minor_items = [
        "Energy Part",
        "Energy Tank",
        "Missile Tank",
        "Missile+ Tank",
        "Power Bomb Tank",
        "Speed Booster Upgrade",
        "Flash Shift Upgrade",
        "Nothing",
    ]
    special_configurations = []
    victory_key = "Metroid DNA"
