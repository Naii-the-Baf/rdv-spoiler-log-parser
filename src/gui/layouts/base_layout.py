class BaseLayout:
    background: dict[str, str]
    foreground: dict[str, str]
    fallback_background: str
    fallback_foreground: str
    victory_background: str

    def __init__(self):
        self.background = {}
        self.foreground = {}
        self.fallback_background = "black"
        self.fallback_foreground = "white"
        self.victory_background = "green"
