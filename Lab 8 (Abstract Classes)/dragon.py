import entity
import random


class Dragon(entity.Entity):
  '''Represents a dragon with a basic and special attack 
  Attributes:
  other : the Hero
  '''

  def basic_attack(self, other):
    """Description: deals damage to the Hero
    Input: other(hero)
    Output/Return: returns a string describing what happened"""
    damage = random.randint(3, 7)
    other.take_damage(damage)
    return self._name + " smashes you with its tail for "+ str(damage) + " damage!"
  
  def special_attack(self, other):
    """Description: deals damage to the Hero
    Input: other(hero)
    Output/Return: returns a string describing what happened"""
    damage = random.randint(4, 8)
    other.take_damage(damage)
    return self._name + " slashes you with its claws for "+ str(damage) + " damage!"
