from ships import letters, numbers, directions, ships_more_then_one, ship_one
from crud import writer, clear_boards
from file_names import ai_board, template_file
import random

def get_ai_ships():
    ships_more_one = 4
    ships_one = 2
    ships_cordinates = []
    while ships_more_one > 1:
        get_init_cordinate = get_users_cordinate()
        get_direction = get_user_direction()
        new_ships = ships_more_then_one(ships_cordinates, get_init_cordinate, get_direction, ships_more_one)
        if new_ships:
            ships_cordinates.extend(new_ships)
            ships_more_one -= 1
    while ships_one > 0:
        get_init_cordinate = get_users_cordinate()
        new_ships_one = ship_one(ships_cordinates, get_init_cordinate)
        if new_ships_one:
            ships_cordinates.append(new_ships_one)
            ships_one -= 1
    clear_boards(template_file, ai_board)
    writer(ai_board, ships_cordinates,"O")
    return ships_cordinates

def get_users_cordinate():
    cordinates = ""
    col = random.choice(letters)
    row = random.choice(numbers)
    return cordinates + col + row

def get_user_direction():
    return random.choice(directions)