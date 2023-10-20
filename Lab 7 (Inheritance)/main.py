# Names: Lesley Del Cid and Kathryn Woest
# Date: 10/05/23
# Description: A simplified version of the card game Blackjack. Objective of the game is to have the highest score without going over the value of 21 to win the round.

import check_input
import player
import dealer
import deck


def display_winner(pScore, dScore, points):
  '''Discription: dsisplays the winner of the round based on the player's hand and the dealer's hand score '''
  if pScore > 21:
    pScore = 0
  if pScore > dScore:
    print("\nPlayer wins!")
    points[0] += 1
  elif pScore < dScore:
    print("\nDealer wins.")
    points[1] += 1
  else:
    print("\nTie")
  print("Player's points:", points[0])
  print("Dealer's points:", points[1])
  

def main():
  #creating a deck and shuffling the deck
  game_deck = deck.Deck()
  game_deck.shuffle()
  total_points = [0, 0]
  quit = False
  print('\n-Blackjack-')

  #our games loop
  while quit is False:
    #initialize the deck to reset
    bust = False
    if len(game_deck) < 15:
      game_deck = deck.Deck()
      game_deck.shuffle()

    #player's first turn 
    player1 = player.Player(game_deck)
    print("\nPlayer's Cards: ")
    print(player1)
    print("Score =", player1.score())
    #check if play's first turn is a bust
    if player1.score() > 21:
        print("Bust!")
        bust = True
    user_choice = check_input.get_int_range('1. Hit \n2. Stay \nEnter Choice: ',1,2)

    #player's loop until they bust or wish to stay with their hand
    while user_choice == 1 and bust == False:
      player1.hit()
      print("\nPlayer's Cards: ")
      print(player1)
      print("Score =", player1.score())

      if player1.score() > 21:
        print("Bust!")
        bust = True
        break
      
      user_choice = check_input.get_int_range('1. Hit \n2. Stay \nEnter Choice: ',1,2)
    
    #dealer's turn to play    
    dealer1 = dealer.Dealer(game_deck)
    dealer1.play()
    
    display_winner(player1.score(), dealer1.score(), total_points)

    #check if the player wishes to play again
    play_again = check_input.get_yes_no('Play again? (Y/N): ')

    if not play_again:
      quit = True
  
main()