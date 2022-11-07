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
    self.__element_number = 0

  def __balance_calculator(self, position):
    # Caluculate the balance factor of a node
    # Initialize height of both children to 0
    left_height = 0
    right_height = 0
    if position.left is not None:
      left_height = position.left.height
    if position.right is not None:
      right_height = position.right.height
    # Compute balabce
    balance = right_height - left_height
    return balance

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

  def __rotate_left(self, position):
    # record the node to be returned
    new_root = position.right
    # update position of floator
    position.right = new_root.left
    new_root.left = position
    self.__update_height(position)
    self.__update_height(new_root)
    return new_root

  def __rotate_right(self, position):
    # record the node to be returned
    new_root = position.left
    # update position of floator
    position.left = new_root.right
    new_root.right = position
    self.__update_height(position)
    self.__update_height(new_root)
    return new_root

  def __balance(self, position):
    # Compute the balance of a node
    balance = self.__balance_calculator(position)
    # if the tree is right heavy
    if balance == 2:
      # check if need double rotation
      if self.__balance_calculator(position.right)<0:
        position.right = self.__rotate_right(position.right)
      return self.__rotate_left(position)
    # if the tree is left heavy
    elif balance == -2:
      # check if need double rotation
      if self.__balance_calculator(position.left)>0:
        position.left = self.__rotate_left(position.left)
      return self.__rotate_right(position)
    else:
      self.__update_height(position)
      return position

  # The private recursive function used to insert element
  def __rec_insert_element(self, value, position):
    if position is None:
      new_node = self.__BST_Node(value)
      return new_node
    elif value < position.value:
      position.left = self.__rec_insert_element(value,position.left)
      return self.__balance(position)
    elif value > position.value:
      position.right = self.__rec_insert_element(value,position.right)
      return self.__balance(position)
    else:
      raise ValueError

  # The public insert function
  def insert_element(self, value):
    self.__root = self.__rec_insert_element(value,self.__root)
    self.__element_number += 1

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
        return self.__balance(position)
    elif position.value > value:
      # find the value recursively
      position.left = self.__rec_remove_element(value, position.left)
      self.__update_height(position)
      return self.__balance(position)
    else:
      # find the value recursively
      position.right = self.__rec_remove_element(value,position.right)
      self.__update_height(position)
      return self.__balance(position)
  
  # The public removal function
  def remove_element(self, value):
    self.__root = self.__rec_remove_element(value,self.__root)
    self.__element_number -= 1

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

  # recursive function to get the list representation
  def __rec_to_list(self, position):
    if position is None:
      # Only change the given list
      # Nothing should be returned
      return 
    else:
      self.__rec_to_list(position.left)
      self.__list[self.__cur] = position.value
      self.__cur += 1
      self.__rec_to_list(position.right)
      # Only change the given list
      # Nothing should be returned
      return 
      
  # public function to get the list representation
  def to_list(self):
    # Initialize the list and index to insert
    self.__cur = 0
    self.__list = [None] * self.__element_number
    self.__rec_to_list(self.__root)
    return self.__list


# if __name__ == '__main__':