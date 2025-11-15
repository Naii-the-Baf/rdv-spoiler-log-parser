from games.game import Game


class Prime3Game(Game):
    major_items = {
        "Beams": [
            "Power Beam",
            "Plasma Beam",
            "Nova Beam",
            "Progressive Beam",
            "Charge Beam",
        ],
        "Missile Systems": [
            "Missile Launcher",
            "Ice Missile",
            "Seeker Missile",
            "Progressive Missile",
        ],
        "Visors": [
            "Combat Visor",
            "Scan Visor",
            "Command Visor",
            "X-Ray Visor",
        ],
        "Morph Upgrades": [
            "Morph Ball",
            "Boost Ball",
            "Spider Ball",
            "Morph Ball Bombs",
        ],
        "Suits": [
            "Hazard Shield",
        ],
        "Movement Systems": [
            "Space Jump Boots",
            "Screw Attack",
        ],
        "Hypermode Upgrades": [
            "Hypermode",
            "Hyper Ball",
            "Hyper Missile",
            "Hyper Grapple",
        ],
        "Grapple Upgrades": [
            "Grapple Lasso",
            "Grapple Swing",
            "Grapple Voltage",
        ],
        "Ship Upgrades": [
            "Ship Missile",
            "Ship Grapple",
        ],
    }
    minor_items = [
        "Energy Tank",
        "Missile Expansion",
        "Ship Missile Expansion",
        "Nothing",
    ]
    special_configurations = []
    victory_key = "Energy Cell"
