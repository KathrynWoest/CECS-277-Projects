import door
import random

class LockedDoor(door.Door):

  def __init__(self):
    self._key_location = random.randint(1,3)
    self._input = 0

  def examine_door(self):
    """Description: describes the door
    Input: N/A
    Return: a string description of the door"""
    
    return "\nA locked door. Look around for the key."

  def menu_options(self):
    """Description: returns the menu options
      Input: N/A
      Return: a string of the menu options the user can choose from to try and unlock the door"""
    
    return "1.Look under the mat \n2.Look under the flower pot \n3.Look under the fake rock"

  def get_menu_max(self):
    """Description: returns the max number of menu options
      Input: N/A
      Return: the max number of menu options"""
    
    return 3
    
  def attempt(self, option):
    """Description: completes the user's choice and updates door attributes as necessary
      Input: which choice the user selected
      Return: a string describing their action"""
    
    if option == 1:
      self._input = 1
      return "You looked under the mat." 
    if option == 2:
      self._input = 2
      return "You looked under the flower pot."
    if option == 3:
      self._input = 3
      return "You looked under the fake rock."

  def is_unlocked(self):
    """Description: determines if the door is unlocked
      Input: N/A
      Return: True if the door is unlocked and False if the door is locked"""
    
    if self._input == self._key_location:
      return True
    else:
      return False

  def clue(self):
    """Description: gives the user a clue if the door is still locked
      Input: N/A
      Return: a string that gives a clue"""
    
    if self._input != self._key_location:
      return "Look somewhere else."

  def success(self):
    """Description: tells the user they unlocked the door
      Input: N/A
      Return: a string describing how the door unlocks"""
    
    return "Congratulations, you found the key and unlocked the door."
