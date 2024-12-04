from gui.layouts.base_layout import BaseLayout

class Prime1Style(BaseLayout):
    def __init__(self):
        super().__init__()
        
        self.background = {
            'Chozo Ruins': '#d8c4af',
            'Magmoor Caverns': '#dd7e6b',
            'Phazon Mines': '#b4a7d6',
            'Phendrana Drifts': '#bfbfbf',
            'Tallon Overworld': '#9fbc93',
        }
        
        self.foreground = {
            'Chozo Ruins': 'black',
            'Magmoor Caverns': 'black',
            'Phazon Mines': 'black',
            'Phendrana Drifts': 'black',
            'Tallon Overworld': 'black',
        }
        
        self.victory_background = '#17baba'