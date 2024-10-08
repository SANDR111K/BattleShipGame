from project import user_shoot
from unittest.mock import patch
from user_init_ships import get_users_cordinate
from ships import ships_more_then_one, ship_one
from crud import opener

@patch("builtins.input", side_effect=["A1"])
def something(monck_input):
    return get_users_cordinate()

#The first pytest
#This function tests function named "get_user_cordinate".
@patch("builtins.input", side_effect=["A1","B4","H7"])
def test_get_users_cordinate(monck_input):
    assert get_users_cordinate() == "A1"
    assert get_users_cordinate() == "B4"
    assert get_users_cordinate() == "H7"

#The second pytest.
#This function tests function named "ships_more_then_one".
def test_ships_more_then_one():
    assert ships_more_then_one(["A1"], "A1", "h", 2) == False
    assert ships_more_then_one([], "A1", "h", 2) == ["A1","B1"]

#The third pytest.
#this function tests funcion called "ship_one".
def test_ship_one():
    assert ship_one(["A1"], "A1") == False
    assert ship_one(["B2"], "H7") == "H7"

#The forth pytest.
#this funcion tests function opener from file "crud.py"
def test_opener():
    assert opener("template.csv") == [[' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
                                      ['1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ''],
                                      ['2', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ''],
                                      ['3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ''],
                                      ['4', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ''],
                                      ['5', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ''],
                                      ['6', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ''],
                                      ['7', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ''],
                                      ['8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '']]