from games.game import Game


class Prime3Game(Game):
    major_items = [
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
    minor_items = [
        "Energy Tank",
        "Missile Expansion",
        "Ship Missile Expansion",
        "Nothing",
    ]
    nothing_item = "Nothing"
    special_configurations = []
    victory_key = "Energy Cell"
