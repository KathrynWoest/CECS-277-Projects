#name: Lesley Del Cid & Kathryn Woest
#date: 8/22/23
#description: number guessing game

import random
import check_input

def main():
  rand_num = int(random.random() * 100)
  user_num = 0
  user_tries = 0
  
  print("- Guessing Game -\nI'm thinking of a number. ", end="")
  user_num = check_input.get_int_range("Make a guess (1-100): ", 1, 100)
  
  while user_num != rand_num:
    
    # if guess is too low:
    if rand_num > user_num:
      user_tries +=1
      print("Too low! ", end="")
      user_num = check_input.get_int_range("Guess again (1-100): ", 1, 100)
      
    # if guess is too high:  
    elif rand_num < user_num:
      user_tries +=1
      print("Too high! ", end="")
      user_num = check_input.get_int_range("Guess again (1-100): ", 1, 100)
    
  # if guess is correct:
  user_tries += 1
  print(f"Correct! You got it in {user_tries} tries.")
  

main()
