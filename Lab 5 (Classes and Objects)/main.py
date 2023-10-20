# Names: Lesley Del Cid and Kathryn Woest
# Date: 9/21/23
# Description: Creates a rectangle by a given width and height. Allows the user to move the rectangle on a 20 by 20 grid. 

import check_input
import rectangle


def display_grid(grid):
  '''Description: pass in the grid and display the contents of the grid
  input: N/A
  returns: N/A'''
  
  for row in grid:
    display = ""
    for column in row:
      display += column
    print(display)


def reset_grid(grid):
  '''Description: overwrites the contents of the grid with "."
  input: N/A
  returns: N/A'''
  
  for row in range(20):
    for column in range(20):
      grid[row][column] = "."


def place_rect(grid, rect):
  '''Description: reads the coordinates of the rectangle on the grid and overwrites the "." with "*" by using the width and height of the rectangle
  input: N/A
  returns: N/A'''
  
  location = rect.get_coords()
  dimensions = rect.get_dimensions()
  width = dimensions[0]
  height = dimensions[1]
  column = location[0]
  for length_w in range(width):
    row = location[1]
    for length_h in range(height):
      grid[row][column] = "*"
      row += 1
    column += 1
    

def main():
  option5 = False 
  # sets up a 20x20 2D list filled with "."
  main_grid = []
  for row in range(20):
    sublist = []
    for column in range(20):
      sublist.append(".")
    main_grid.append(sublist)

  # gets width and height and sets up the rectangle object
  w = check_input.get_int_range("Enter rectangle width (1-5): ",1,5)
  h = check_input.get_int_range("Enter rectangle height (1-5): ",1,5)
  main_rect = rectangle.Rectangle(w,h)

  # places the rect. object, displays it, and resets the 2D list
  place_rect(main_grid, main_rect)
  display_grid(main_grid)
  reset_grid(main_grid)

  # while the user has not quit:
  while not option5:
    print('Enter Direction:')
    print('1. Up')
    print('2. Down')
    print('3. Left')
    print('4. Right')
    print('5. Quit')
    move = check_input.get_int_range('',1,5)

    # moves the rectangle based on the user's input
    coords = main_rect.get_coords()
    if move == 1:
      # checks to make sure the rectangle has space to move
      loc = coords[1] - 1
      if loc < 0:
        print("You cannot move here.")
      else:
        main_rect.move_up()
    elif move == 2:
      loc = coords[1] + main_rect.height + 1
      if loc > 20:
        print("You cannot move here.")
      else:
        main_rect.move_down()
    elif move == 3:
      loc = coords[0] - 1
      if loc < 0:
        print("You cannot move here.")
      else:
        main_rect.move_left()
    elif move == 4:
      loc = coords[0] + main_rect.width + 1
      if loc > 20:
        print("You cannot move here.")
      else:
        main_rect.move_right()
    else:
      option5 = True

    # as long as the user has not quit, print the updated grid
    if not option5:
      place_rect(main_grid, main_rect)
      display_grid(main_grid)
      reset_grid(main_grid)
  

main()
