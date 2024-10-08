from ships import *
from crud import *
from file_names import *

def get_user_ships():
    ships_more_one = 4
    ships_one = 2
    ship_cordinates = []
    while ships_more_one > 1:

        get_init_cordinate = get_users_cordinate()
        get_direction = get_user_direction()
        new_ship = ships_more_then_one(ship_cordinates, get_init_cordinate, get_direction, ships_more_one)
        if new_ship:
            ship_cordinates.extend(new_ship)
            ships_more_one -= 1
            writer(user_file, ship_cordinates, "O")
            printer()
        else:
            print("Impossible to create the ship")
    while ships_one > 0:
        get_init_cordinate = get_users_cordinate()
        new_ship_one = ship_one(ship_cordinates, get_init_cordinate)
        if new_ship_one:
            ship_cordinates.append(new_ship_one)
            ships_one -= 1
            writer(user_file, ship_cordinates, "O")
            printer()
        else:
            print("Impossible to create the ship")

    clear_boards(template_file, user_file)
    writer(user_file, ship_cordinates, "O")
    return ship_cordinates

def get_users_cordinate():
    while True:
        user  = input("Add ship init cordinate (eg. A1 or C2 and so on): ")
        if len(user)==2:
            col, row = list(user)
            if col.upper() in letters and row in numbers:
                return user.upper()
            else:
                print("Incorrect cordinate format")
        else:
            print("Wrong Cordinates")

def get_user_direction():
    while True:
        user = input("Give the direction of the ship (eg. v or h): ").lower()
        if user in directions:
            return user
        else:
            print("Incorrect directions")