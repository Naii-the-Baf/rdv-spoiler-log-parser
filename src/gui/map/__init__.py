def is_game_map_supported(game_id: str) -> bool:
    match game_id:
        case "am2r":
            return False
        case "dread":
            return False
        case "fusion":
            return True
        case "prime1":
            return False
        case "prime2":
            return True
        case "prime3":
            return False
        case _:
            return False
