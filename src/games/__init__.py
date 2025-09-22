from games import am2r_game, dread_game, fusion_game, game, prime1_game, prime2_game, prime3_game


def get_game_by_id(game_id: str) -> game.Game:
    match game_id:
        case "am2r":
            return am2r_game.AM2RGame()
        case "dread":
            return dread_game.DreadGame()
        case "fusion":
            return fusion_game.FusionGame()
        case "prime1":
            return prime1_game.Prime1Game()
        case "prime2":
            return prime2_game.Prime2Game()
        case "prime3":
            return prime3_game.Prime3Game()
        case _:
            return game.NotSupportedGame()
