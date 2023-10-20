import door
import random

class DeadboltDoor(door.Door):
  def __init__(self):
    b1 = random.randint(1, 2)
    if b1 == 1:
      self._bolt1 = True
    else:
      self._bolt1 = False
    b2 = random.randint(1, 2)
    if b2 == 1:
      self._bolt2 = True
    else:
      self._bolt2 = False

  def examine_door(self):
    """Description: describes the door
    Input: N/A
    Return: a string description of the door"""
    
    return "\nA door with two deadbolts. Both need to be unlocked to open the door, but you can't tell if each one is locked or unlocked."

  def menu_options(self):
    """Description: returns the menu options
      Input: N/A
      Return: a string of the menu options the user can choose from to try and unlock the door"""

    return "1. Toggle bolt 1\n2. Toggle bolt 2"

  def get_menu_max(self):
    """Description: returns the max number of menu options
      Input: N/A
      Return: the max number of menu options"""

    return 2

  def attempt(self, option):
    """Description: completes the user's choice and updates door attributes as necessary
      Input: which choice the user selected
      Return: a string describing their action"""

    if option == 1:
      self._bolt1 = not self._bolt1
      return "You toggle the first bolt."
    else:
      self._bolt2 = not self._bolt2
      return "You toggle the second bolt."

  def is_unlocked(self):
    """Description: determines if the door is unlocked
      Input: N/A
      Return: True if the door is unlocked and False if the door is locked"""

    if self._bolt1 and self._bolt2:  # if both bolts are unlocked
      return True
    else:
      return False

  def clue(self):
    """Description: gives the user a clue if the door is still locked
      Input: N/A
      Return: a string that gives a clue"""

    if self._bolt1 or self._bolt2:  # if one of the bolts is unlocked
      return "You jiggle the door...it seems like one of the bolts is unlocked."
    else:  # if both are locked
      return "You jiggle the door...it seems like it's completely locked."

  def success(self):
    """Description: tells the user they unlocked the door
      Input: N/A
      Return: a string describing how the door unlocks"""

    return "You unlocked both deadbolts and opened the door."
