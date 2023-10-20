# Names: Lesley Del Cid and Kathryn Woest
# Date: 9/07/23
# Description: A two-player dice game Ship, Captian, and Crew. Each player rolls a set of 5 dice up to three turns. The player must get a 6, 5, and a 4 in that order first. The remaining two dice will be added as points. The player whith the highest score wins.

import check_input
import random

def roll_dice(dice):
  """Description: rolls dice and sorts the results in descending order
Input: original set of dice (so we know how many to roll)
Output: none"""
  
  for i in range(len(dice)):
    roll = random.randint(1, 6)
    dice[i] = roll
  dice.sort()
  dice.reverse()

def find_winner(player_points):
  """Description: compares the final scores of each player and prints out who won the game/if it was a tie
Input: the scores of each player at the end of the game
Output: prints the results of the game"""

  score1 = player_points[0]
  score2 = player_points[1]
  print('\nScore:')
  print(f'Player #1 = {score1}')
  print(f'Player #2 = {score2}')
  if score1 > score2:
    print('Player #1 won!')
  elif score2 > score1:
    print('Player #2 won!')
  else:
    print("Player #1 and Player #2 tied!")

def display_dice(name, dice):
  """Description: formats and displays the dice roll/cargo/keep lists
Input: the name of the list (name) and the contents of the list (dice)
Output: prints the dice roll/cargo/keep"""
  
  dice_format = ""
  for i in dice:
    dice_format += f"{str(i)} "
  print(f'{name}: {dice_format}')
  

def main():
  #initailizing the varables
  player_turns = 3
  play_again = True

  print("- Ship, Captain, and Crew! –")

  keep = []
  scores = [0, 0]

  for turn in range(2):
    print(f"\nPlayer #{turn + 1}'s Turn:")
    #Loops player's turn until they run out of turns or request to end their turn
    while player_turns > 0 and play_again == True :
      #Check how many dice should be rolled. For every keep we find we must remove a dice
      if len(keep) == 0:
        dice_roll = [0, 0, 0, 0, 0]
      elif len(keep) == 1:
        dice_roll = [0, 0, 0, 0]
      elif len(keep) == 2:
        dice_roll = [0, 0, 0]
      else:
        dice_roll = [0, 0]
  
      #calling the functions to roll a dice and display if a keep was found
      roll_dice(dice_roll)
      display_dice("Roll", dice_roll)

      # if a 6 is in the roll and has not been obtained yet
      if dice_roll[0] == 6 and 6 not in keep:
        keep.append(6)
        dice_roll.pop(0)
        print('Yo ho ho! Ye secured a ship!')
    
      # if 5 is in the roll, has not been obtained yet, and a 6 is obtained
      if 6 in keep and 5 not in keep:
        for i in range(len(dice_roll)):
          if dice_roll[i] == 5:
            keep.append(5)
            dice_roll.pop(i)
            print('Shiver me timbers! A Capt’n!')
            break
    
      # if 4 is in the roll, has not been obtained yet, and a 6/5 is obtained
      if 6 in keep and 5 in keep and 4 not in keep:
        for i in range(len(dice_roll)):
          if dice_roll[i] == 4:
            keep.append(4)
            dice_roll.pop(i)
            print('Ye bribed a crew with Grog!')
            break
              
      display_dice("Keep", keep)
    
    # if 6/5/4 have been kept, calculate and display cargo points
      if len(keep) == 3:
        display_dice("Cargo", dice_roll)
      
      #updating the player's scores in a list 
      player_score = 0
      if len(keep) == 3:
        for i in dice_roll:
          player_score += i
        print(f"Your cargo points are: {player_score}")  
      scores[turn] = player_score
      player_turns -= 1
  
      #prompts the user if they wish to roll again
      if player_turns != 0:
        play_again = check_input.get_yes_no("\nRoll again? ")
  
    # once the player is done, print their total score
    if play_again == False or player_turns == 0:
      if turn == 0:
        print(f'Player #1 points = {scores[0]}')
      else:
        print(f'Player #2 points = {scores[1]}')

    # reinitializes variables for next player
    player_turns = 3
    play_again = True
    keep = []
    
  #calls the function find_winner to print the winner to the user
  find_winner(scores)
  
main()