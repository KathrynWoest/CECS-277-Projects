class Task:
  '''Represents List of task that must be completed
  Attributes:
  desc : The description of the task
  date : The due date of the task list
  time : The time the task is due 
  '''
  
  def __init__(self, desc, date, time):
    self.description = desc
    self.date = date
    self.time = time
    
  def __str__ (self):
    '''String representation of a task - user facing.'''
    return self.description + " - Due: " + self.date +" at "+ self.time
    
  def __repr__(self):
    '''String representation of a task - file facing.'''
    return self.description + "," + self.date +","+ self.time
    
  def __lt__(self,other):
    '''Description: returns true if the task is less then the other task by comparing year, month, day, hour, minute, and then by alphabetical order'''

  #sets the values into integers to be able to compare which task is due first
    full_date = self.date
    month = int(full_date[0:2])
    day = int(full_date[3:5])
    year = int(full_date[6:10])
    time =  self.time
    hour = int(time[0:2])
    min = int(time[3:5])

    #'other task' is also being set to integers to be compared 
    full_other = other.date
    month_o = int(full_other[0:2])
    day_o = int(full_other[3:5])
    year_o = int(full_other[6:10])
    time_other =  other.time
    other_hour = int(time_other[0:2])
    other_min = int(time_other[3:5])

  #first sort by year, and if those are the same, it should sort by month, then day, then hour, then minute, then if all of those are the same, then sort by the description
    if year < year_o:
      return True
      
    elif year > year_o:
      return False

    else:
      if month < month_o:
        return True
      
      elif month > month_o:
        return False
        
      else:  
        if day < day_o:
          return True
          
        elif day > day_o:
          return False
          
        else:
          if hour < other_hour:
            return True
            
          elif hour > other_hour: 
            return False
            
          else:
            if min < other_min:
              return True
            elif min > other_min:
              return False
            else:  
              if self.description.lower() < other.description.lower():
                return True
              else:
                return False
      