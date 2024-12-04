from gui.layouts.base_layout import BaseLayout

class Prime2Style(BaseLayout):
    def __init__(self):
        super().__init__()
        
        self.background = {
            'Agon Wastes': '#fff2cc',
            'Dark Agon Wastes': '#783f04',
            'Dark Torvus Bog': '#38761d',
            'Ing Hive': '#1155cc',
            'Great Temple': '#d5a6bd',
            'Sanctuary Fortress': '#9fc5e8',
            'Sky Temple Grounds': '#351c75',
            'Temple Grounds': '#b4a7d6',
            'Torvus Bog': '#b6d7a8',
        }
        
        self.foreground = {
            'Agon Wastes': 'black',
            'Dark Agon Wastes': 'white',
            'Dark Torvus Bog': 'white',
            'Ing Hive': 'white',
            'Great Temple': 'black',
            'Sanctuary Fortress': 'black',
            'Sky Temple Grounds': 'white',
            'Temple Grounds': 'black',
            'Torvus Bog': 'black',
        }