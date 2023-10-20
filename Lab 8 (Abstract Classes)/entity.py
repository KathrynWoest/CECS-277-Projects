import abc


class Entity(abc.ABC):
  '''Represents a creature (hero or dragon) and their necessary characteristics 
  Attributes:
  name : name of the creature
  max_hp : the maximum health of the creature
  hp : the current health of the creature
  '''
  
  def __init__(self, name, max_hp):
    self._name = name
    self._hp = max_hp
    self._max_hp = max_hp

  @property
  def name(self):
    return self._name

  @property
  def hp(self):
    return self._hp

  def take_damage(self, dmg):
    """Description: deals damage to the creature by decreasing their hp
    Input: N/A
    Output/Return: N/A"""
    self._hp -= dmg
    if self._hp < 0:  # if the creature's hp goes below 0, reset to 0
      self._hp = 0
  
  def __str__(self):
    return f"{self._name}: {self._hp}/{self._max_hp}"

  @abc.abstractmethod
  def basic_attack(self, other):
    pass

  @abc.abstractmethod
  def special_attack(self, other):
    pass
  