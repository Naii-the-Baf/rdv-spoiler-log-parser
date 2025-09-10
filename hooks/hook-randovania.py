from __future__ import annotations

from pathlib import Path

from PyInstaller.utils.hooks import collect_data_files
from randovania.cli import database
from randovania.game.game_enum import RandovaniaGame
from randovania.games import default_data
from randovania.lib.enum_lib import iterate_enum

datas = []

# We need to remove the 'randovania' directory from the target, as rdv only looks for a specific path
for source, target in collect_data_files(
    "randovania.games", includes=["**/migration_data.json", "**/pickup-database.json", "**/presets/**"]
):
    target = target[11:]
    datas.append((source, target))

# This will generate the database binaries, as they are not included in the randovania package.
# Code taken from randovania's create_release.py, found at
# https://github.com/randovania/randovania/blob/da9a326ad5e74ac88f47a29a7e7e8c6b1d081a36/tools/create_release.py#L177-L181
root = Path(__file__).parents[1]

if not Path.exists(root.joinpath("data")):
    root.joinpath("data").mkdir()

for game in iterate_enum(RandovaniaGame):
    file_path = root.joinpath("data", f"{game.value}.bin")
    database.export_as_binary(
        default_data.read_json_then_binary(game)[1],
        file_path,
    )
    datas.append((file_path, "data/binary_data"))
