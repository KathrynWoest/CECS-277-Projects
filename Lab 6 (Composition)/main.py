# Names: Lesley Del Cid and Kathryn Woest
# Date: 9/28/23
# Description: Maintains a task list provided by the user and allows the user to view, remove, and add tasks.


import task
import tasklist
import check_input


def main_menu():
  """Description: prints the main menu and gets the user's choice
    Inputs: N/A
    Output/Return: the user's choice"""
  
  print("1. Display current task")
  print("2. Display all tasks")
  print("3. Mark current task complete")
  print("4. Add new task")
  print("5. Save and quit")
  choice = check_input.get_int_range("Enter choice: ", 1, 5)
  return choice

def get_date():
  """Description: gets the date of a new task
    Inputs: N/A
    Output/Return: the user's date as a string, formatted MM/DD/YYYY"""
  
  print("Enter due date:")
  month = check_input.get_int_range("Enter month: ", 1, 12)
  day = check_input.get_int_range("Enter day: ", 1, 31)
  year = check_input.get_int_range("Enter year: ", 2000, 3000)

  # if month/day is less then 10, add a 0 at the front for formatting
  # then convert each integer into a string
  if month < 10:
    month = "0" + str(month)
  else:
    month = str(month)

  if day < 10:
    day = "0" + str(day)
  else:
    day = str(day)

  year = str(year)

  return f"{month}/{day}/{year}"
  

def get_time():
  """Description: gets the time of a new task
    Inputs: N/A
    Output/Return: the user's time as a string, formatted HH:MM"""
  
  print("Enter time:")
  hour = check_input.get_int_range("Enter hour: ", 0, 23)
  minute = check_input.get_int_range("Enter minute: ", 0, 59)

  # if hour/minute is less then 10, add a 0 at the front for formatting
  # then convert each integer into a string
  if hour < 10:
    hour = "0" + str(hour)
  else:
    hour = str(hour)

  if minute < 10:
    minute = "0" + str(minute)
  else:
    minute = str(minute)  

  return f"{hour}:{minute}"

def main():
  user_tasklist = tasklist.Tasklist()
  run_main = True

  while run_main:
    
    print("\n-Tasklist-")
    print(f"Tasks to complete: {len(user_tasklist)}")
    user_choice = main_menu()

#calls the approprite functions based the the users choice from the main menu selections
    if user_choice == 1:
      if len(user_tasklist) > 0:
        current_task = user_tasklist[0]
        print(current_task)
      else:
        print('All tasks are complete!')
      
    elif user_choice == 2:
      if len(user_tasklist) > 0:
        for i in range(len(user_tasklist)):
          print(user_tasklist.task_list[i])
      else:
        print("All tasks are complete!")
        
    elif user_choice == 3:
      if len(user_tasklist) > 0:
        print("Marking current task as complete:", user_tasklist[0])
        user_tasklist.mark_complete()
        print("New current task is:", user_tasklist[0])
      else:
        print("All tasks are complete!")
        
    elif user_choice == 4:
      desc = input("Enter a task: ")
      date = get_date()
      time = get_time()
      user_tasklist.add_task(desc, date, time)
      
    elif user_choice == 5:
      user_tasklist.save_file()
      run_main = False


main()