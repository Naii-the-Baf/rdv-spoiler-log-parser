import game

class World:
    def __init__(self, world):
        self.game_id = world['game']
        self.game = None
        self.items = world['locations']
        
        match self.game_id:
            case 'prime2':
                self.game = game.Prime2
                
            case _:
                pass
        
    def GetItemLocations(self):
        return self.items
