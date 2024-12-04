import argparse

class ArgParser:
    def __init__(self):
        self.parser = self.define_args()
        self.args = self.parser.parse_args()
        
    def define_args(self):
        self.parser = argparse.ArgumentParser(description = "Parses a spoiler log file produced by Randovania, and returns a view of item locations.")
        self.parser.add_argument('-f', '--file', required=False)
        return self.parser
        
    def get_args(self):
        return self.args
