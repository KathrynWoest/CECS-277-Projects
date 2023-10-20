import task


class Tasklist:
  '''Creates and modifies a list of task objects
  Attributes:
  task_list : the list of task objects, intially derived from a given file
  '''
  
  
  def __init__(self):
    self.task_list = []
    file = open("tasklist.txt")
    for line in file:
      # creates a task object for each stripped/split line in the file
      line = line.strip("\n")
      task_split = line.split(",")
      task_object = task.Task(task_split[0], task_split[1], task_split[2])
      self.task_list.append(task_object)
    file.close()
    self.task_list.sort()

  def add_task(self, desc, date, time):
    """Description: creates a new task object, appends it to the task list, and then resorts the task list
    Inputs: description, date, and time of the new task
    Output/Return: N/A"""
    new_task = task.Task(desc, date, time)
    self.task_list.append(new_task)
    self.task_list.sort()

  def mark_complete(self):
    """Description: takes the current task out of the task list
    Inputs: N/A
    Output/Return: N/A"""
    # rewrites task_list to not include the first (current) task object
    self.task_list = self.task_list[1:]

  def save_file(self):
    """Description: saves the current task list into the file
    Inputs: N/A
    Output/Return: N/A"""
    file = open("tasklist.txt", "w")
    for task_item in self.task_list:
      # for each task object, write it to a line in the file
      file.write(repr(task_item) + "\n")
    file.close()

  def __getitem__(self, index):
    """Description: returns the task object at the given index in the list
    Inputs: the index of the desired task object
    Output/Return: the task object at the index"""
    return self.task_list[index]

  def __len__(self):
    """Description: returns the number of tasks in the task list (length of the list)
    Inputs: N/A
    Output/Return: the length of the task list"""
    return len(self.task_list)
