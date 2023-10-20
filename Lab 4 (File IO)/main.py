# Names: Lesley Del Cid and Kathryn Woest
# Date: 9/14/23
# Description: program that opens a maze from a file and has the user solve the maze by moving in the indicated direction

import check_input


def read_maze():
  """Description: reads the maze from the given file and formats it into a 2D list
Input: N/A
Returns: the 2D list that contains the maze"""
  
  maze_file = open("maze.txt")
  maze = []
  for row in maze_file:  # for each line in the file, create a list
      list = []
      for item in row:  # for each character in the line, append to the list
          if item != '\n':
              list.append(item)
      maze.append(list)
  maze_file.close()
  return maze


def find_start(maze):
  """Description: finds the starting location in the maze
Input: the 2D list that contains the maze
Returns: the starting location in a list"""
  
  start_location = [0, 0]
  row_count = 0
  for row in maze:
    column_count = 0
    for column in row:  # for each item in the 2D list, check if it's "s"
      if column == "s":
        start_location = [row_count, column_count]
      column_count += 1
    row_count += 1
  return start_location


def display_maze(maze, loc):
  """Description: formats and displays the maze and the user's current location
Input: the maze as a 2D list and the user's location as a 1D list
Output: prints the maze and the user's location"""

  row_count = 0
  for row in maze:
    column_count = 0
    print_row = ""  # create a string for each row in the maze
    for column in row:
      # if the item in the row is where the user is
      if row_count == loc[0] and column_count == loc[1]:
        print_row += "X"  # add "X" to the string instead of the item itself
      else:
        print_row += column
      column_count +=1
    print(print_row)  # print out each row in the maze
    row_count += 1


def main():

  maze = read_maze()
  user_loc = find_start(maze)
  
  finish = False
  print('-Maze Solver-')

  # while the user has not finished the maze
  while finish is False:

    # print the maze, menu, and prompt
    display_maze(maze, user_loc)
    print('1. Go North')
    print('2. Go South')
    print('3. Go East')
    print('4. Go West')
    user_choice = check_input.get_int_range("Enter choice: ",1,4)

    # moves the user if possible
    if user_choice == 1: 
      if maze[user_loc[0] - 1][user_loc[1]] == "*":
        print('You cannot move there.')
      else:
        user_loc[0] -= 1
        
    elif user_choice == 2: 
      if maze[user_loc[0] + 1][user_loc[1]] == "*":
        print('You cannot move there.')
      else:
        user_loc[0] += 1
        
    elif user_choice == 3: 
      if maze[user_loc[0]][user_loc[1] + 1] == "*":
        print('You cannot move there.')
      else:
        user_loc[1] += 1 
        
    else: 
      if maze[user_loc[0]][user_loc[1] - 1] == "*":
        print('You cannot move there.')
      else:
        user_loc[1] -= 1

    # if the user finishes the maze:
    if maze[user_loc[0]][user_loc[1]] == "f":
      display_maze(maze, user_loc)
      print('Congratulations! You solved the maze.')
      finish = True


main()  