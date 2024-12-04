# Randovania Spoiler Log Parser
NOTE: This is still a work in progress; it may or may not work.
___

Reads a spoiler file produced by [Randovania](https://github.com/randovania/randovania), and returns a view of items. The purpose of this tool is to make spoiler logs easily and quickly readable, primarily for spoiler log races.

A tool for this purpose was [made previously using Google Sheets](https://docs.google.com/spreadsheets/d/1JTMr1bqu33ng2b5X9IVmFFgltN88k8Bi6Ee8h4d8a3s/edit?gid=1414799479#gid=1414799479); and this is a rework of it as a python application, as it has become increasingly more difficult to maintain as new games are added.

## Running from source

1. Create a python venv:
`python -m venv .venv`

2. Activate the venv:
Windows: `call .venv\scripts\bin\Activate`
Unix: `source .venv/bin/activate`

3. Install the dependencies:
`pip install -r requirements.txt`

4. Run the application:
`python main.py`
