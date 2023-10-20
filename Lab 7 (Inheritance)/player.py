class Player:
  '''Represents the user, their attributes, and their possible actions 
  Attributes:
    _deck: the deck that the user is playing with
    _hand: a list of the cards in the user's hand
  '''
  
  def __init__(self, deck):
    self._deck = deck
    self._hand = [self._deck.draw_card(), self._deck.draw_card()]
    self._hand.sort()

  def hit(self):
    """Description: draws a card and adds it to the player's hand, then sorts the hand
       Input: N/A
       Output/Return: N/A"""
    
    self._hand.append(self._deck.draw_card())
    self._hand.sort()

  def score(self):
    """Description: calculates the score of the player's hand
       Input: N/A
       Output/Return: the score of the player's hand"""
    
    total_score = 0
    for card in self._hand:
      if card._rank <= 8:  # if the card is a number card (2 - 10)
        total_score += card._rank + 2  # add that card's number to the score
      elif 9 <= card._rank <= 11:  # if the card is a face card (J - K)
        total_score += 10  # add ten to the score
      else:  # if the card is an ace
        if total_score < 22:
          total_score += 11  # add eleven to the score if the score is < 22
        else:
          total_score += 1  # add one to the score if the score is >= 22
    return total_score

  def __str__(self):
    """Description: returns a string representation of the cards in the player's hand
       Input: N/A
       Output/Return: the user's hand, formatted as a string"""
    
    hand = ""
    for card in range(len(self._hand) - 1):  # add each card to a string format
      hand += f"{str(self._hand[card])}\n"
    hand += f"{str(self._hand[-1])}"
    return hand
