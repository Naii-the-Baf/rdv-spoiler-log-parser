from gui.layouts.base_layout import BaseLayout


class FusionStyle(BaseLayout):
    def __init__(self):
        super().__init__()

        self.background = {
            "Main Deck": "#b7b7b7",
            "Sector 1 (SRX)": "#fae99a",
            "Sector 2 (TRO)": "#b7dba8",
            "Sector 3 (PYR)": "#d77b6e",
            "Sector 4 (AQA)": "#aabef4",
            "Sector 5 (ARC)": "#d2e1f3",
            "Sector 6 (NOC)": "#b5a2d6",
        }

        self.foreground = {
            "Main Deck": "black",
            "Sector 1 (SRX)": "black",
            "Sector 2 (TRO)": "black",
            "Sector 3 (PYR)": "black",
            "Sector 4 (AQA)": "black",
            "Sector 5 (ARC)": "black",
            "Sector 6 (NOC)": "black",
        }

        self.victory_background = "#0ce561"
