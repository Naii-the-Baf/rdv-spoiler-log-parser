import game

class World:
    def __init__(self, world):
        self.game_id = world['game']
        self.game : game.Game = None
        self.items : dict = world['locations']
        
        match self.game_id:
            case 'prime2':
                self.game = game.Prime2()
                
            case _:
                pass
        
    def GetItemLocations(self):
        major_items = dict() #Name: [(region, room, reference)]
        minor_items = dict()
        for category in self.game.major_items:
            for item in category:
                major_items[item] = []
        
        for item in self.game.minor_items:
            minor_items[item] = []
        
        if self.game.has_regions:
            for region, locations in self.items.items():
                for location, pickup in locations.items():
                    room, ref_item = location.split("/Pickup ")
                    if room is None or ref_item is None:
                        raise ValueError("Error while reading spoiler: Invalid item location: " + location + " " + pickup)
                    if pickup in minor_items:
                        #Minor
                        minor_items[pickup].append((region, room, ref_item))
                    elif pickup in major_items:
                        #Major
                        major_items[pickup].append((region, room, ref_item))
                    else:
                        raise ValueError("Error while reading spoiler: Invalid pickup: " + location + " " + pickup)
        else:
            pass
        return (major_items, minor_items)
