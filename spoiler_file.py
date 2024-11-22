import json

class SpoilerFile:
    def __init__(self):
        self.json = None
        self.objects = None
        
    def Read(self, filename):
        with open(filename, "r") as file:
            self.json = json.load(file)
            file.close()
        
                   
    def GetItems(self):
        return self.json