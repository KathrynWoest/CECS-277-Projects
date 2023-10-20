# Names: Lesley Del Cid and Kathryn Woest
# Date: 10/12/23
# Description: a mash-up game of HTTYD and D&D. Defeat three dragons to pass dragon training.

import check_input
import hero
import dragon
import flying_dragon
import fire_dragon
import random


def main():
  hero_name = input("What is your name, challenger?\n")

  # initalize a hero object and a list of dragon objects
  user_hero = hero.Hero(hero_name, 50)
  dragon_list = [dragon.Dragon("Deadly Nadder", 10), fire_dragon.Fire_dragon("Gronckle", 15), flying_dragon.Flying_dragon("Timberjack", 20)]
  win = False
  
  print("Welcome to dragon training,", hero_name)
  print("You must defeat 3 dragons.")

  while not win:
    print(f"\n{user_hero}")
    for i in range(len(dragon_list)):  # for each dragon in the list, print them in the menu
      print(f"{i + 1}. Attack {dragon_list[i]}")

    dragon_choice = check_input.get_int_range("Choose a dragon to attack: ", 1, len(dragon_list))

    print("\nAttack with:")
    print("1. Sword (2 D6)")
    print("2. Arrow (1 D12)")
    weapon_choice = check_input.get_int_range("Enter weapon: ", 1, 2)

    if weapon_choice == 1:  # if the hero chooses a sword attack:
      print(user_hero.basic_attack(dragon_list[dragon_choice-1]))
    else:  # if the hero chooses an arrow attack
      print(user_hero.special_attack(dragon_list[dragon_choice-1]))

    # if the dragon dies, remove it from the list
    if dragon_list[dragon_choice-1].hp == 0:
      dragon_list.pop(dragon_choice - 1)

    if len(dragon_list) == 0:
      print("Congratulations! You have defeated all 3 dragons, you have passed the trials.")
      win = True
      
    else:
      # randomly select a dragon to attack and a type of attack
      rand_dragon = random.randint(0, len(dragon_list) - 1)
      rand_attack = random.randint(1, 2)

      if rand_attack == 1:  # if the dragon uses a basic attack:
        print(dragon_list[rand_dragon].basic_attack(user_hero))
      else:  # if the dragon uses a special attack:
        print(dragon_list[rand_dragon].special_attack(user_hero))

    if user_hero.hp == 0:
      #if the user dies before they kill all the dragons
      print("Sorry, you passed out and lost the trials.")
      win = True


main()
