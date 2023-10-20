import player


class Dealer(player.Player):
  '''Represents the dealer, their attributes, and their possible actions 
    Attributes:
     _deck: the deck that the user is playing with (inherited from Player)
     _hand: a list of the cards in the user's hand (inherited from Player)
  '''

  def play(self):
    """Description: plays the Dealer's turn, hitting when their score is less than 17 and staying when their score is more than 16.  Prints their hand, their score, and their action every turn
       Input: N/A
       Output/Return: prints the dealer's hand, score, and if they busted"""
    
    # print the dealer's cards and their score
    score = 0
    print("\nDealer's Cards:")
    print(self)
    score = self.score()
    print("Score =", score)
    
    while score <= 16:  # while their score is less than 17, have the dealer hit
      print("Dealer Hits!")
      self.hit()
      score = self.score()
      print("\nDealer's Cards:")
      print(self)
      print("Score =", score)
      
    if score > 21:  # if the dealer's score ends up > 21, they bust
      print("Bust!")
      self._hand = []  # empty their hand so that calculating their score --> 0
