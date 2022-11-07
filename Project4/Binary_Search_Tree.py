class Binary_Search_Tree:

  class __BST_Node:

    def __init__(self, value):
      self.value = value # initialize the value
      self.height = 1 # initialize height to be 1
      self.left = None # a new node does not have left or right child
      self.right = None

  def __init__(self):
    # Initialize the root attribute to None
    self.__root = None


  # Function used to update the height of each node
  # after insertion or removal
  def __update_height(self, position):
    if position.left is None and position.right is None:
      # A node with no children has height 1
      position.height = 1
    elif position.left is None:
      # If it does not have left child, height = height of right child + 1
        position.height = position.right.height + 1
    elif position.right is None:
      # If it does not have right child, height = height of left child + 1
      position.height = position.left.height + 1
    else:
      # If has two children, height = heigher child + 1
      position.height = position.left.height + 1
      if position.right.height > position.left.height:
        position.height = position.right.height + 1

  # The private recursive function used to insert element
  def __rec_insert_element(self, value, position):
    if position is None:
      new_node = self.__BST_Node(value)
      return new_node
    elif value < position.value:
      position.left = self.__rec_insert_element(value,position.left)
      self.__update_height(position)
      return position
    elif value > position.value:
      position.right = self.__rec_insert_element(value,position.right)
      self.__update_height(position)
      return position
    else:
      raise ValueError

  # The public insert function
  def insert_element(self, value):
    self.__root = self.__rec_insert_element(value,self.__root)

  
  # The private function that can locate the smallest value in a tree
  # Useful in removal
  def __small_value_locator(self, position):
    if position.left is None:
      return position.value
    else: 
      return self.__small_value_locator(position.left)

  # The private recursive function used to remove element
  def __rec_remove_element(self, value, position):
    if position is None:
      # No value found
      raise ValueError
    elif position.value == value:
      # Value found
      if position.left is None and position.right is None:
        return
      elif position.left is None:
        return position.right
      elif position.right is None:
        return position.left
      else:
        smallest_value = self.__small_value_locator(position.right)
        # change the value to the smallest value in the right sub-tree
        position.value = smallest_value
        # remove the duplicate value
        position.right = self.__rec_remove_element(smallest_value, position.right)
        return position
    elif position.value > value:
      # find the value recursively
      position.left = self.__rec_remove_element(value, position.left)
      self.__update_height(position)
      return position
    else:
      # find the value recursively
      position.right = self.__rec_remove_element(value,position.right)
      self.__update_height(position)
      return position
  
  # The public removal function
  def remove_element(self, value):
    self.__root = self.__rec_remove_element(value,self.__root)

  # Private recursive function to get the in_order string representation
  def __rec_in_order(self, position):
    rec_string = ''
    if position is None:
      # if nothing is there, return empty string
      return ''
    else:
      rec_string += self.__rec_in_order(position.left) 
      if position.left is not None:
        # add required format
        rec_string += ', '
      rec_string += str(position.value)
      if position.right is not None:
        # add required format
        rec_string += ', '
      rec_string += self.__rec_in_order(position.right)
      return rec_string

  # Public function to get the in_order representation
  def in_order(self):
    height = self.get_height()
    if height == 0:
      return '[ ]'
    string = '[ '
    string += self.__rec_in_order(self.__root)
    string += ' ]'
    return string


  # Private recursive function to get the pre_order string representation
  def __rec_pre_order(self, position):
    rec_string = ''
    if position is None:
      # if nothing is there, return empty string
      return ''
    else:
      rec_string += str(position.value)
      if position.left is not None:
        # add required format
        rec_string += ', '
      rec_string += self.__rec_pre_order(position.left) 
      if position.right is not None:
        # add required format
        rec_string += ', '
      rec_string += self.__rec_pre_order(position.right)
      return rec_string

  # Public function to get the pre_order representation
  def pre_order(self):
    height = self.get_height()
    if height == 0:
      return '[ ]'
    string = '[ '
    string += self.__rec_pre_order(self.__root)
    string += ' ]'
    return string

  # Private recursive function to get the post_order string representation
  def __rec_post_order(self, position):
    rec_string = ''
    if position is None:
      # if nothing is there, return empty string
      return ''
    else:
      rec_string += self.__rec_post_order(position.left) 
      if position.left is not None:
        # add required format
        rec_string += ', '
      rec_string += self.__rec_post_order(position.right)
      if position.right is not None:
        # add required format
        rec_string += ', '
      rec_string += str(position.value)
      return rec_string

  # Public function to get the post_order representation
  def post_order(self):
    if self.__root is None:
      return '[ ]'
    string = '[ '
    string += self.__rec_post_order(self.__root)
    string += ' ]'
    return string

  def get_height(self):
    if self.__root is None:
      return 0
    return self.__root.height

  def __str__(self):
    return self.in_order()

# if __name__ == '__main__':
