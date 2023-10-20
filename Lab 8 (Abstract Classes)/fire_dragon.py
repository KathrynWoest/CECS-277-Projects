import dragon
import random


class Fire_dragon(dragon.Dragon):
  '''Represents a Fire dragon with a special attack 
  Attributes:
  name : name of the dragon
  max_hp : hp left in the dragon
  F_shots : special attacks of the dragon
  '''

  def __init__(self, name, max_hp, f_shots=3):
    super().__init__(name, max_hp)
    self.f_shots = f_shots

  def special_attack(self, other):
    """Description: deals damage to the Hero
    Input: other(hero)
    Output/Return:returns a string describing what happened"""
    if self.f_shots > 0:
      damage = random.randint(5,9)
      other.take_damage(damage)
      self.f_shots -= 1
      return self.name + " engulfs you in flames for "+ str(damage) + " damage!"
    else:
      return self.name + " tries to spit fire at you but is all out of fire shots."

  def __str__(self):
    return super().__str__() + "\nFire Shots remaining: " + str(self.f_shots)





    