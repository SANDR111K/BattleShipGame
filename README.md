# BattleShipGame

BattleShipGame is a terminal-based Python implementation of the classic Battleship game. Players compete against an AI to guess ship locations on a grid, with the goal of sinking all enemy ships.

## Features

- **Player vs AI**: Battle against a computer opponent.
- **Random Ship Placement**: AI ships are randomly placed.
- **Terminal-Based Gameplay**: Interact via command-line.
- **File Persistence**: Ships and game states are stored using CSV files.
- **CRUD Operations**: Save and load game data.

## Project Structure

```plaintext
|-- ai_init_ships.py        # AI ship placement logic
|-- crud.py                 # CRUD operations for game state
|-- file_names.py           # File path constants
|-- project.py              # Main game logic
|-- ships.py                # Ship class and methods
|-- user_init_ships.py      # Player ship placement logic
|-- test_project.py         # Test cases
|-- csv_files/              # CSV files for game data
