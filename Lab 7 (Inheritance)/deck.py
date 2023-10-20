import card
import random


class Deck:
  '''Represents a deck of cards 
  Attributes:
    _cards: a list of the 52 cards in a standard deck
  '''
  
  def __init__(self):
    self._cards = []
    for suit in range(4):  # for each possible suit
      for rank in range(13):  # for each possible rank
        self._cards.append(card.Card(suit, rank))  # add the card to the deck

  def shuffle(self):
    """Description: shuffles the deck
       Input: N/A
       Output/Return: N/A"""
    
    random.shuffle(self._cards)

  def draw_card(self):
    """Description: draws the top card from the deck and removes it from the deck
       Input: N/A
       Output/Return: the top card"""
    
    top_card = self._cards[0]
    self._cards = self._cards[1:]  # reset the deck to not include the first/top card
    return top_card

  def __len__(self):
    """Description: returns the length of the deck (ex: full deck = 52 cards)
       Input: N/A
       Output/Return: the number of cards in the deck"""
    
    return len(self._cards)
