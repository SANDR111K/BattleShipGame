import random
from file_names import *
from ai_init_ships import *
from user_init_ships import *
from ships import *
from user_init_ships import *
from crud import *

def main():
    prepare_init_tables()
    print("\nWelcome to Buttleship Game.\n")
    print("Your enemy is ready.\n")
    get_ai_ships()
    print("Now is your time to generate ships.\n")
    user_cordinates = get_user_ships()
    printer()
    print(f"" "\n" "OK!!! lets start the game." "\n" "")

    enemy_cordinates = get_enemy_and_user_cordinates(ai_board)
    user_board_coordinates = get_enemy_and_user_cordinates(user_file)

    fired_list_for_user = []
    fired_list_for_ai   = []

    while len(enemy_cordinates) > 0 and len(user_board_coordinates) > 0:
        user_shoots = user_shoot(enemy_cordinates)
        fired_list_for_user.append(user_shoots)

        if user_shoots[1]:
            if user_shoots[0] not in fired_list_for_user:
                enemy_cordinates.remove(user_shoots[0])
                writer(enemy_file, [user_shoots[0]], "X")
                printer()
            else:
                print("You already use this coordinate. try another.")
                continue
        else:
            writer(enemy_file, [user_shoots[0]], "-")
            printer()

        enemy_shoots = enemy_shoot(user_board_coordinates)
        fired_list_for_ai.append(enemy_shoots)

        if enemy_shoots[1]:
            if enemy_shoots[0] not in fired_list_for_ai:
                user_board_coordinates.remove(enemy_shoots[0])
                writer(user_file, [enemy_shoots[0]], "X")
                printer()
            else:
                continue
        else:
            writer(user_file, [enemy_shoots[0]], "-")
            printer()
    if len(enemy_cordinates) > 0:
        print("You lose try again.")
    elif len(user_board_coordinates) > 0:
         print("You win congratulations <3")

def get_enemy_and_user_cordinates(board):
    data = opener(board)
    cordinates_tuple = []
    final_cordinates = []
    for rows in range(len(data)):
        for cols in range(len(data[rows])):
            if data[rows][cols] == "O":
                cordinates_tuple.append((cols, rows))
    for x,y in cordinates_tuple:
        temp = ""
        temp+= letters[x-1]
        temp+=str(y)
        final_cordinates.append(temp)
    return final_cordinates


def prepare_init_tables():
    clear_boards(template_file, enemy_file)
    clear_boards(template_file, ai_board)
    clear_boards(template_file, user_file)

def user_shoot(enemy_cordinates):
    shoot = get_users_cordinate()
    if shoot in enemy_cordinates:
        return shoot, True
    else:
        return shoot, False

def enemy_shoot(user_cordinat):
    shoot_col = random.choice(letters)
    shoot_row = random.choice(numbers)
    enemy_shoot = shoot_col + shoot_row
    if enemy_shoot in user_cordinat:
        return enemy_shoot, True
    else:
        return enemy_shoot, False

if __name__=="__main__":
    main()