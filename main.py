from arg_parser import ArgParser
from spoiler_file import SpoilerFile

parser = ArgParser()
args = parser.GetArgs()

spoiler = SpoilerFile()
spoiler.Read(args.file)
items = spoiler.GetItems()

print(items['info']['presets'][0]["game"])