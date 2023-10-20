class Card:
  '''Represents a deck of cards 
  Attributes:
  rank : list of the cards value
  suit : list of the card types
  '''
  
  
  def __init__(self, suit, rank):
    self._suit = suit
    self.rank = rank

  @property
  def rank(self):
    return self._rank

  @rank.setter
  def rank(self, rank):
    if type(rank) == int:
      if 12 >= rank >= 0:
        self._rank = rank
      else:
        raise ValueError("Rank must be a positive integer between 0 and 12.")
    else:
      raise TypeError("Rank must be a number.")
      
  def __str__(self):
    '''Description: String representation of the cards value and type of card'''
    
    rank_list = ['2', '3', '4', '5', '6', '7', '8','9', '10', 'Jack', 'Queen', 'King', 'Ace' ]
    suit_list = ['Clubs', 'Diamonds', 'Hearts', 'Spades'] 

    return  rank_list[self._rank] + " of " + suit_list[self._suit]

  def __lt__(self, other):
    '''Description: returns true if if the self rank is less than the other rank'''
    
    if self._rank < other._rank:
      return True
    else:
      return False
