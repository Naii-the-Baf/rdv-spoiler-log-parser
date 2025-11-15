from games.game import Game


class Prime1Game(Game):
    major_items = {
        "Beams": [
            "Power Beam",
            "Wave Beam",
            "Ice Beam",
            "Plasma Beam",
            "Charge Beam",
        ],
        "Missiles + Beam Combos": [
            "Super Missile",
            "Wavebuster",
            "Ice Spreader",
            "Flamethrower",
            "Missile Launcher",
        ],
        "Visors": [
            "Combat Visor",
            "Scan Visor",
            "Thermal Visor",
            "X-Ray Visor",
        ],
        "Morph Upgrades": [
            "Morph Ball",
            "Boost Ball",
            "Spider Ball",
            "Morph Ball Bomb",
            "Power Bomb",
        ],
        "Suits": [
            "Varia Suit",
            "Gravity Suit",
            "Phazon Suit",
        ],
        "Movement Systems": [
            "Space Jump Boots",
            "Grapple Beam",
        ],
    }
    minor_items = [
        "Energy Tank",
        "Missile Expansion",
        "Power Bomb Expansion",
        "Energy Refill",
        "Missile Refill",
        "Power Bomb Refill",
        "Nothing",
    ]
    special_configurations = []
    victory_key = "Artifact of"
