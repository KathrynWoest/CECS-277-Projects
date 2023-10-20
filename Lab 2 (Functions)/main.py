#name: Lesley Del Cid and Kathryn Woest
#Date: 8/29/2023
#description: Three card Monte game that allows a player to place a bet and guess the location of the queen card in a set of three cards.

import check_input
import random

def get_users_bet(money):
  """description: prints the user's money and asks the user how much money they want to bet
     input: user money and bet
     returns: the user's bet"""
  
  print(f"You have ${money}.")
  bet = check_input.get_int_range("How much you wanna bet? ", 1, money)
  return bet

def get_users_choice():
  """description: prints the cards face down and asks for the user's guess
     input: user guess
     returns: user guess"""
  
  print('+-----+ +-----+ +-----+')
  print('|     | |     | |     |')
  print('|  1  | |  2  | |  3  |')
  print('|     | |     | |     |')
  print('+-----+ +-----+ +-----+')
  
  #returns the card the user wishes to bet on. 
  users_guess = check_input.get_int_range("Find the queen: ",1,3)
  return users_guess


def display_queen_loc(queen_loc):
  """description: prints the visual location of the queen after the user's choice
     input: the queen's location
     outputs: the cards face up"""
  
  if queen_loc == 1:
    print('+-----+ +-----+ +-----+')
    print('|     | |     | |     |')
    print('|  Q  | |  K  | |  K  |')
    print('|     | |     | |     |')
    print('+-----+ +-----+ +-----+')
  elif queen_loc == 2:
    print('+-----+ +-----+ +-----+')
    print('|     | |     | |     |')
    print('|  K  | |  Q  | |  K  |')
    print('|     | |     | |     |')
    print('+-----+ +-----+ +-----+')
  else:
    print('+-----+ +-----+ +-----+')
    print('|     | |     | |     |')
    print('|  K  | |  K  | |  Q  |')
    print('|     | |     | |     |')
    print('+-----+ +-----+ +-----+')


def main():
  users_money = 100
  play_again = "Y"

  while users_money > 0 and play_again == "Y":
    
    # calls for the functions
    queen_location = random.randint(1, 3)
    users_bet = get_users_bet(users_money)
    user_loc_guess = get_users_choice()
    display_queen_loc(queen_location)
    
    # checks if the user's guess was correct and prints if it was correct or not
    if user_loc_guess == queen_location:
      users_money += users_bet
      print("You got lucky this time...")
      
    else:
      users_money -= users_bet
      print("Sorry... you lose.")

    #checks if the user is able or wants to play again based on the amount of money left
    if users_money > 0:
      user_play = input("Play again? (Y/N): ")
      print("\n")
      play_again = user_play.upper()

      #checks if the input for play again is valid to the parameters of "Y" and "N"
      while play_again != "Y" and play_again != "N":
        print("Invalid input. Please select 'Y' or 'N'.")
        user_play = input("Play again? (Y/N): ")
        play_again = user_play.upper()
        print("\n")
        
    else:
      print("You're out of money. Beat it loser!")

main()