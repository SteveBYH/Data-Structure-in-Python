class Linked_List:
  
  class __Node:
    
    def __init__(self, val):
      self._next = None
      self._previous = None
      self._value = val

  def __init__(self):
    self.__header = self.__Node(None)
    self.__trailer = self.__Node(None)
    self.__header._next = self.__trailer
    self.__trailer._previous = self.__header
    self.__size = 0

  def __len__(self):
    return self.__size

  def append_element(self, val):
    new_node = self.__Node(val)
    new_node._next = self.__trailer
    self.__trailer._previous._next = new_node
    new_node._previous = self.__trailer._previous
    self.__trailer._previous = new_node
    self.__size = self.__size + 1


  def insert_element_at(self, val, index):
    if index >= self.__size or index<0:
        raise IndexError
    else:
        new_node = self.__Node(val)
        if index < self.__size/2:
            # If the index is closer to the header
            # Iterate from the header node
            current = self.__header
            for i in range(index):
                current = current._next
            new_node._next = current._next
            current._next._previous = new_node
            current._next = new_node
            new_node._previous = current
        else: 
            # If the index is closer to the trailer
            # Iterate from the trailer node
            current = self.__trailer
            for i in range(self.__size-index):
                current = current._previous
            new_node._next = current
            current._previous._next = new_node
            new_node._previous = current._previous
            current._previous = new_node
        self.__size += 1
    
  def remove_element_at(self, index):
    if index >= self.__size or index<0 :
        raise IndexError
    else:
        if index < self.__size/2:
            # If the index is closer to the header
            # Iterate from the header node
            current = self.__header
            for i in range(index):
                current = current._next
            returned = current._next._value
            current._next._next._previous = current
            current._next = current._next._next
            self.__size -= 1
            return returned

        else:
            # If the index is closer to the trailer
            # Iterate from the trailer node
            current = self.__trailer
            for i in range(self.__size - index - 1):
                current = current._previous
            returned = current._previous._value
            current._previous._previous._next = current
            current._previous = current._previous._previous
            self.__size -= 1
            return returned
            
  def get_element_at(self, index):
    if index >= self.__size or index<0:
        raise IndexError
    else: 
        if index < self.__size/2:
            # If the index is closer to the header
            # Iterate from the header node
            current = self.__header._next
            for i in range(index):
                current = current._next
            return current._value
        else: 
            # If the index is closer to the trailer
            # Iterate from the trailer node
            current = self.__trailer
            for i in range(self.__size - index):
                current = current._previous
            return current._value

  def rotate_left(self):
    if self.__size == 0 or self.__size == 1:
        return
        
    else:
        # Record the first node which would be rotated to the back
        current = self.__header._next
        # Link header to the second node in the linked list
        self.__header._next = self.__header._next._next
        self.__header._next._previous = self.__header
        # Put the recorded node to the last position of the linked list
        current._next = self.__trailer
        self.__trailer._previous._next = current
        current._previous = self.__trailer._previous
        self.__trailer._previous = current

  def __str__(self):
    string = "["
    current = self.__header._next
    number_of_element = 1
    while current != self.__trailer:
        if number_of_element >=2:
            string += ","
        string += " "
        string += str(current._value)
        current = current._next
        number_of_element = number_of_element + 1
    string += " ]"
    return string
    
  def __iter__(self):
    # Initialize the position of the element to be iterated
    self.__iterator = self.__header._next
    return self

  def __next__(self):
    if self.__iterator == self.__trailer:
      raise StopIteration
    to_return = self.__iterator._value
    self.__iterator = self.__iterator._next
    return to_return

