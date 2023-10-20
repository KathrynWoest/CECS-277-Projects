class Rectangle:
  '''Represents a rectangle on the coordinate plane.
  Attributes:
  x (int): location x of the rectangle.
  y (int): location y of the rectangle.
  width (int): width of the rectangle.
  height (int): height of the rectangle.
  '''
  def __init__(self,w,h):
    self.x = 0
    self.y = 0
    self.width = w
    self.height = h

  def get_coords(self):
    '''Description: returns self.x and self.y in a coordinate list'''
    coords = [self.x, self.y]
    return coords
    
  def get_dimensions(self):
    '''Description: returns the dimension of the rectangle in a list'''
    dimension = [self.width, self.height]
    return dimension
  
  def move_up(self):
    '''Description: shifts the y coordinate up'''
    self.y -= 1 
    
  def move_down(self):
    '''Description: shifts the y coordinate down'''
    self.y += 1
    
  def move_left(self):
    '''Description: shifts the x coordinate left'''
    self.x -= 1
    
  def move_right(self):
    '''Description: shifts the x coordinate right'''
    self.x += 1
    