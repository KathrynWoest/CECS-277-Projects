# Names: Lesley Del Cid and Kathryn Woest
# Date: 10/19/23
# Description: An escape room game. The user must escape 3 doors in order to escape

import check_input
import deadboltDoor
import basicDoor
import lockedDoor
import random


def open_door(door):
  """Description: completes all necessary actions for the user to unlock the given door
  Inputs: the object representing the door, the user's choice
  Outputs: prints the door's methods/attributes and what the user is doing"""
  
  success = False
  print(door.examine_door()) # print door description
  while not success:  # while door isn't open
    print(door.menu_options())  # print menu
    user_choice = check_input.get_int_range("", 1, door.get_menu_max())  # get user choice
    print(door.attempt(user_choice))  # print user's action
    if door.is_unlocked():  # if the door unlocks
      print(door.success()) # print the success
      success = True
    else:
      print(door.clue())  # print a clue


def main():
  print("Welcome to the Escape Room. You must unlock 3 doors to escape...")
  
  door = [basicDoor.BasicDoor(), deadboltDoor.DeadboltDoor(), lockedDoor.LockedDoor()]

  for i in range(3):
    rand_door = random.randint(0, 2)
    open_door(door[rand_door])
    
  print('Congratulations! You escaped...this time.')
main()