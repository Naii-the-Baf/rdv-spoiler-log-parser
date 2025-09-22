class Game:
    major_items: list = []
    minor_items: list = []
    nothing_item: str = "Nothing"
    special_configurations: list = []
    victory_key: str = "A default victory key"


class NotSupportedGame(Game):
    pass
