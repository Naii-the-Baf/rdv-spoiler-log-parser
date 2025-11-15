from games.game import Game


class Prime2Game(Game):
    major_items = {
        "Beams": [
            "Power Beam",
            "Dark Beam",
            "Light Beam",
            "Annihilator Beam",
            "Charge Beam",
        ],
        "Missile Systems": [
            "Missile Launcher",
            "Seeker Launcher",
        ],
        "Beam Combos": [
            "Super Missile",
            "Darkburst",
            "Sunburst",
            "Sonic Boom",
        ],
        "Visors": [
            "Combat Visor",
            "Scan Visor",
            "Dark Visor",
            "Echo Visor",
        ],
        "Morph Upgrades": [
            "Morph Ball",
            "Boost Ball",
            "Spider Ball",
            "Morph Ball Bomb",
            "Power Bomb",
        ],
        "Suits": [
            "Dark Suit",
            "Light Suit",
            "Progressive Suit",
        ],
        "Movement Systems": [
            "Space Jump Boots",
            "Gravity Boost",
            "Grapple Beam",
            "Screw Attack",
            "Progressive Grapple",
        ],
        "Translators": [
            "Violet Translator",
            "Amber Translator",
            "Emerald Translator",
            "Cobalt Translator",
        ],
        "Temple Keys": [
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
        "Cheater's Delights": ["Cannon Ball", "Double Damage", "Unlimited Beam Ammo", "Unlimited Missiles"],
    }
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
