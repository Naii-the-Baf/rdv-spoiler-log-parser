from games.game import Game


class FusionGame(Game):
    major_items = {
        "Beams": [
            "Charge Beam",
            "Wide Beam",
            "Plasma Beam",
            "Wave Beam",
            "Ice Beam",
        ],
        "Missile Systems": [
            "Missile Launcher Data",
            "Super Missile Data",
            "Ice Missile Data",
            "Diffusion Missile Data",
        ],
        "Morph Upgrades": [
            "Morph Ball",
            "Morph Ball Bomb Data",
            "Power Bomb Data",
        ],
        "Suits": [
            "Varia Suit",
            "Gravity Suit",
        ],
        "Misc": [
            "Hi-Jump",
            "Space Jump",
            "Speed Booster",
            "Screw Attack",
        ],
        "Keycards": [
            "Level 1 Keycard",
            "Level 2 Keycard",
            "Level 3 Keycard",
            "Level 4 Keycard",
        ],
    }
    minor_items = [
        "Energy Tank",
        "Missile Tank",
        "Power Bomb Tank",
        "Nothing",
    ]
    special_configurations = []
    victory_key = "Infant Metroid"
