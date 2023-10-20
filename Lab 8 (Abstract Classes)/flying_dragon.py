import dragon
import random


class Flying_dragon(dragon.Dragon):
  '''Represents a Flying dragon with a special attack 
  Attributes:
  name : name of the dragon
  max_hp : hp left in the dragon
  swoops : special attacks of the dragon
  '''
  def __init__(self, name, max_hp, swoops=5):
    super().__init__(name, max_hp)
    self.swoops = swoops
    
  def special_attack(self,other):
    """Description: deals damage to the Hero
    Input: other(hero)
    Output/Return:returns a string describing what happened"""
    if self.swoops > 0:
      damage = random.randint(5,8)
      other.take_damage(damage)
      self.swoops -= 1
      return self.name + " swoops at you for "+ str(damage) + " damage!"
    else:
      return self.name + " tries to swoop down to hit you, but failed."
    
  def __str__(self):
    return super().__str__()  + "\nSwoop attacks remaining: " +  str(self.swoops)

