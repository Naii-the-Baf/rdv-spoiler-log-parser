from gui.styles import am2r_style, base_style, dread_style, fusion_style, prime1_style, prime2_style, prime3_style


def get_style_for_game(game_id: str) -> base_style.BaseStyle:
    match game_id:
        case "am2r":
            return am2r_style.AM2RStyle()
        case "dread":
            return dread_style.DreadStyle()
        case "fusion":
            return fusion_style.FusionStyle()
        case "prime1":
            return prime1_style.Prime1Style()
        case "prime2":
            return prime2_style.Prime2Style()
        case "prime3":
            return prime3_style.Prime3Style()
        case _:
            return base_style.NotSupportedStyle()
