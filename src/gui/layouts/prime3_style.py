from gui.layouts.base_layout import BaseLayout

class Prime3Style(BaseLayout):
    def __init__(self):
        super().__init__()
        
        self.background = {
            'Bryyo - Fire': '#f9944a',
            'Bryyo - Ice': '#cfe2f3',
            'Bryyo - Reptilicus': '#9fbc93',
            'Bryyo - Seed': '#3c78d8',
            'G.F.S. Olympus': '#8eafce',
            'G.F.S. Valhalla': '#d5a6bd',
            'Norion': '#bfbfbf',
            'Pirate Homeworld - Command': '#dd7e6b',
            'Pirate Homeworld - Mines': '#4dc923',
            'Pirate Homeworld - Research': '#cc4125',
            'Pirate Homeworld - Seed': '#3c78d8',
            'SkyTown, Elysia - Main': '#d8c4af',
            'SkyTown, Elysia - Pod': '#f9cb9c',
            'SkyTown, Elysia - Seed': '#3c78d8',
        }
        
        self.foreground = {
            'Bryyo - Fire': 'black',
            'Bryyo - Ice': 'black',
            'Bryyo - Reptilicus': 'black',
            'Bryyo - Seed': 'white',
            'G.F.S. Olympus': 'black',
            'G.F.S. Valhalla': 'black',
            'Norion': 'black',
            'Pirate Homeworld - Command': 'black',
            'Pirate Homeworld - Mines': 'black',
            'Pirate Homeworld - Research': 'white',
            'Pirate Homeworld - Seed': 'white',
            'SkyTown, Elysia - Main': 'black',
            'SkyTown, Elysia - Pod': 'black',
            'SkyTown, Elysia - Seed': 'white',
        }
        
        self.victory_background = '#0ce561'