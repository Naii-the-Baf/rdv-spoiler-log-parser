from games.game import Game


class AM2RGame(Game):
    major_items = [
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
    minor_items = [
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
        "Nothing",
    ]
    nothing_item = "Nothing"
    special_configurations = []
    victory_key = "Metroid DNA"
