from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    
    self.__capacity = 1 # The capacity of the array stroing the data
    self.__contents = [None] * self.__capacity
    self.__front = 0 # The position of the front in the array
    self.__back = 0 # The position of the back in the array
    self.__size = 0 # The size of the deque
    
  def __str__(self):
    string = "["
    current = self.__front
    if self.__size == 0:
      # if the size is 0, return the empty braket
      return '[ ]'
    else:
      string += ' '
      # if length is not 0, add the first element
      string += str(self.__contents[self.__front])
      for i in range(self.__size-1):
        # add other elements if there are any
        # add the special formatting
        string += ', '
        string += str(self.__contents[(current+1) % self.__capacity])
        current += 1
    string += ' ]'
    return string
    
  def __len__(self):
    return self.__size

  def __grow(self):
    # create a new array
    content_replace = [None] * self.__capacity * 2 
    to_be_replaced = self.__front # the position of each deque element in the array
    replace = 0 # the position of each deque element in the new array
    for i in range(self.__size):
      # place all the element in the deque in the new array
      content_replace[replace] = self.__contents[to_be_replaced % self.__capacity]
      to_be_replaced += 1
      replace += 1
    
    # Let the new array be the array containing the data
    self.__contents = content_replace 
    self.__capacity = self.__capacity * 2
    self.__front = 0
    self.__back = self.__size - 1


    
  def push_front(self, val):
    if self.__size == self.__capacity:
      # If reach full capacity, first grwo then add
      self.__grow()
      self.__front = self.__capacity - 1
      self.__contents[self.__front] = val
    
    else:
      # Add to the front of the data structure
      self.__front = (self.__front-1) % self.__capacity
      self.__contents[self.__front] = val
    self.__size += 1
    
  def pop_front(self):
    if self.__size == 0:
      # if size is 0, do nothing
      return
    else:
      # pop and return
      to_return = self.__contents[self.__front]
      self.__front = (self.__front+1) % self.__capacity
      self.__size -= 1
      return to_return
    
  def peek_front(self):
    if self.__size == 0:
      # if size is 0, do nothing
      return
    else:
      to_return = self.__contents[self.__front]
      return to_return
    
  def push_back(self, val):
    if self.__size == self.__capacity:
      # if reach full capacity, grow and add
      self.__grow()
      self.__contents[self.__size] = val
      self.__size += 1
      self.__back = self.__size - 1
    else:
      # add directly
      self.__back = (self.__back+1) % self.__capacity
      self.__contents[self.__back] = val
      self.__size += 1
  
  def pop_back(self):
    if self.__size == 0:
      # if size is 0, do nothing
      return
    else:
      # pop and return
      to_return = self.__contents[self.__back]
      self.__back = (self.__back-1) % self.__capacity
      self.__size -= 1
      return to_return

  def peek_back(self):
    if self.__size == 0:
      # if size is 0, do nothing
      return
    to_return = self.__contents[self.__back]
    return to_return

