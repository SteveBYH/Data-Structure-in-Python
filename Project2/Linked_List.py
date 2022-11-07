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

if __name__ == '__main__':
  a = Linked_List()

  # Test the string function and length function when the linked list is empty
  print('The current linked list is: ' + str(a))
  print('The Length of the linked list is: ' + str(len(a)))

  # Test the get_element_at functin when the list is empty
  try:
    print('The last element in the list is: ' + str(a.get_element_at(len(a)-1)))
  except IndexError:
    print('Can not get the element at tail! The linked list is empty!')

  try:
    # Test the append function
    a.append_element(2)
    print('Element appended!')
  except AttributeError:
    print('Wrong attibute in the append function!')
  
  # Test the string function and length function when the size of the list is 1.
  # Here if the Output is [ 2 ] and the size of the linked list is 1, 
  # It also suffices to show that the append function is working.
  print('Now the list is ' + str(a))
  print('The size of the linked list is: ' + str(len(a)))

  # The last element should be 2 and there should not be an index error below
  try:
    print('The last element in the list is: ' + str(a.get_element_at(len(a)-1)))
  except IndexError:
    print('Can not get the element at tail! The linked list is empty!')

  try:
  # Test the get_element_at function with an invalid index when size is 1
    print('The element at index 3 is ' + str(a.get_element_at(3)))
  except IndexError:
    print('The index you want to get is invalid!')

  try:
   # Try to append when the size of the list is 1
    a.append_element(3)
    a.append_element(4)
    print('Element appended!')
  except AttributeError:
    print('Wrong attibute in the append function!')

  # Test the string function and length function when the size of the list is 3.
  print('Now the list is ' + str(a))
  print('The size of the linked list is: ' + str(len(a)))

  # The last element should be 4 and there should not be an index error below
  try:
    print('The last element in the list is: ' + str(a.get_element_at(len(a)-1)))
  except IndexError:
    print('Can not get the element at tail! The linked list is empty!')
  
  try:
    # Test the get_element_at function with a valid index when size is 3
    print('The element at index 0 is ' + str(a.get_element_at(0)))
  except IndexError:
    print('The index you want to get is invalid!')

  try:
    # Test the get_element_at function with an invalid index when size is 3
    print('The element at index 4 is ' + str(a.get_element_at(4)))
  except IndexError:
    print('The index you want to get is invalid!')
  
  # Test the remove function

  try:
    # try to remove at an invalid index when size is 3
    a.remove_element_at(3)
  except IndexError:
    print('Invalid Index For Removing!')
  except AttributeError:
    print('Wrong attibute in the remove function!')
  print('Now the list is ' + str(a))
  print('The size of the linked list is: ' + str(len(a)))

  try:
    # try to remove at a valid index when size is 3
    # First remove in the second half of the linked list
    a.remove_element_at(2)
  except IndexError:
    print('Invalid Index For Removing!')
  except AttributeError:
    print('Wrong attibute in the remove function!')
  print('Now the list is ' + str(a))
  print('The size of the list is ' + str(len(a)))

  try:
    # try to remove at a valid index when size is 2
    # First remove in the first half of the linked list
    a.remove_element_at(0)
  except IndexError:
    print('Invalid Index For Removing!')
  except AttributeError:
    print('Wrong attibute in the remove function!')
  print('Now the list is ' + str(a))
  print('The size of the list is ' + str(len(a)))

  try:
    # try to remove at an invalid index when size is 1
    a.remove_element_at(3)
  except IndexError:
    print('Invalid Index For Removing!')
  except AttributeError:
    print('Wrong attibute in the remove function!')
  print('Now the list is ' + str(a))
  print('The size of the linked list is: ' + str(len(a)))

  try:
    # try to remove at a valid index when size is 1
    a.remove_element_at(0)
  except IndexError:
    print('Invalid Index For Removing!')
  except AttributeError:
    print('Wrong attibute in the remove function!')
  print('Now the list is ' + str(a))
  print('The size of the list is ' + str(len(a)))

  try:
    # try to remove at an invalid index when size is 0
    a.remove_element_at(0)
  except IndexError:
    print('Invalid Index For Removing!')
  except AttributeError:
    print('Wrong attibute in the remove function!')
  print('Now the list is ' + str(a))
  print('The size of the linked list is: ' + str(len(a)))


  # Test the insert_element_at function

  try: 
    # try to insert at an invalid index when size is 0
    a.insert_element_at(2,0)
  except IndexError:
    print('Invalid index of insertion!')
  print('Now the list is ' + str(a))
  print('The size of the linked list is: ' + str(len(a)))

  try:
    # append an element to a so size is 1
    a.append_element(2)
    print('Element appended!')
  except AttributeError:
    print('Wrong attibute!')
  print('Now the list is ' + str(a))
  print('The size of the linked list is: ' + str(len(a)))

  try: 
    # try to insert at an invalid index when size is 1
    a.insert_element_at(3,2)
  except IndexError:
    print('Invalid index of insertion!')
  print('Now the list is ' + str(a))
  print('The size of the linked list is: ' + str(len(a)))

  try: 
    # try to insert at a valid index when size is 1
    a.insert_element_at(3,0)
  except IndexError:
    print('Invalid index of insertion!')
  print('Now the list is ' + str(a))
  print('The size of the linked list is: ' + str(len(a)))

  try:
    # append an element to a so size is 3
    a.append_element(4)
    print('Element appended!')
  except AttributeError:
    print('Wrong attibute!')
  print('Now the list is ' + str(a))
  print('The size of the linked list is: ' + str(len(a)))

  try: 
    # try to insert at an invalid index when size is 3
    a.insert_element_at(3,4)
  except IndexError:
    print('Invalid index of insertion!')
  print('Now the list is ' + str(a))
  print('The size of the linked list is: ' + str(len(a)))

  try: 
    # try to insert at a valid index in the second half when size is 3
    a.insert_element_at(7,2)
  except IndexError:
    print('Invalid index of insertion!')
  print('Now the list is ' + str(a))
  print('The size of the linked list is: ' + str(len(a)))

  try: 
    # try to insert at a valid index in the first half when size is 4
    a.insert_element_at(9,0)
  except IndexError:
    print('Invalid index of insertion!')
  print('Now the list is ' + str(a))
  print('The size of the linked list is: ' + str(len(a)))

  # Test the iterator
  try:
    # Test the iterator when size is 5
    print()
    print('Try interator when size is 5: ')
    for val in a:
      print(val)
    print()
  except AttributeError:
    print('Wrong attribute in the function!')

  # Change size to 1
  try:
    a.remove_element_at(4)
    a.remove_element_at(3)
    a.remove_element_at(2)
    a.remove_element_at(1)
  except IndexError:
    print('Invalid Index For Removing!')

  print('Now the list is ' + str(a))
  print('The size of the linked list is: ' + str(len(a)))
  
  try:
    # Test the iterator when size is 1
    print()
    print('Try interator when size is 1: ')
    for val in a:
      print(val)
    print()
  except AttributeError:
    print('Wrong attribute in the function!')

  # Change size to 0
  try:
    a.remove_element_at(0)
  except IndexError:
    print('Invalid Index For Removing!')

  print('Now the list is ' + str(a))
  print('The size of the linked list is: ' + str(len(a)))

  try:
    # Test the iterator when size is 0
    print()
    print('Try interator when size is 0: ')
    for val in a:
      print(val)
    print()
  except AttributeError:
    print('Wrong attribute in the function!')

  # Test the rotate_left function
  try:
    # Test the retate_left function when size is 0
    a.rotate_left()
    print('The linked list is now: '+ str(a))
  except AttributeError:
    print('Wrong attribute in the function!')

  try:
    # append an element to a so size is 1
    a.append_element(2)
    print('Element appended!')
  except AttributeError:
    print('Wrong attibute!')
  print('Now the list is ' + str(a))
  print('The size of the linked list is: ' + str(len(a)))

  try:
    # Test the retate_left function when size is 1
    a.rotate_left()
    print('The linked list is now: '+ str(a))
  except AttributeError:
    print('Wrong attribute in the function!')

  try:
    # append an element to a so size is 3
    a.append_element(3)
    a.append_element(4)
    print('Element appended!')
  except AttributeError:
    print('Wrong attibute!')
  print('Now the list is ' + str(a))
  print('The size of the linked list is: ' + str(len(a)))

  try:
    # Test the retate_left function when size is 3
    a.rotate_left()
    print('The linked list is now: '+ str(a))
  except AttributeError:
    print('Wrong attribute in the function!')