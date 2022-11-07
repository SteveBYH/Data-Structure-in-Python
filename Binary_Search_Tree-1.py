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
  def __lvalue_loc(self, value, position):
    if value is not None and value is not '_':
      if value < position.value:
        return self.__lvalue_loc(value, position.left)
      elif value > position.value:
        return self.__lvalue_loc(value, position.right)
      else:
        if position.left is not None:
          return position.left.value
        else:
          return None
    else:
      return None

  def height_loc(self, value, position):
    if value is not None and value is not '_':
      if value < position.value:
        self.__height_loc(value, position.left)
      elif value > position.value:
        self.__height_loc(value, position.right)
      else:
        a = position.height
        return a
    else:
      return 0

  def __rvalue_loc(self, value, position):
    if value is not None and value is not '_':
      if value < position.value:
        return self.__rvalue_loc(value, position.left)
      elif value > position.value:
        return self.__rvalue_loc(value, position.right)
      else:
        if position.right is not None:
          return position.right.value
        else:
          return None
    else:
      return None

  def __line_drawer(self, row, col):
    if self.a is not None and self.a is not '_':
      if self.j == self.get_height()-1 and self.__element_number>2**(self.get_height()-2) and self.get_height()>4:
        if self.b is not None and self.b is not '_':
          for k in range (1*2**self.__left_arm(self.a,self.__root)+7):
            self.vis_list[row][col-1-k] = '_'
        if self.c is not None and self.c is not '_':
          for k in range (1*2**self.__right_arm(self.a,self.__root)+7):
            self.vis_list[row][col+1+k] = '_'
      elif self.j == self.get_height()-2 and self.__element_number>2**(self.get_height()-2) and self.get_height()>4:
        if self.b is not None and self.b is not '_':
          for k in range (1*2**self.__left_arm(self.a,self.__root)+3):
            self.vis_list[row][col-1-k] = '_'
        if self.c is not None and self.c is not '_':
          for k in range (1*2**self.__right_arm(self.a,self.__root)+3):
            self.vis_list[row][col+1+k] = '_'
      else:
        if self.b is not None and self.b is not '_':
          for k in range (1*2**self.__left_arm(self.a,self.__root)-1):
            self.vis_list[row][col-1-k] = '_'
        if self.c is not None and self.c is not '_':
          for k in range (1*2**self.__right_arm(self.a,self.__root)-1):
            self.vis_list[row][col+1+k] = '_'

  def __list_upd(self, row, col):
    if self.a is not None and self.a is not '_':
      if self.j == self.get_height()-1 and self.__element_number>2**(self.get_height()-2) and self.get_height()>4:
        if self.b is not None:
          self.vis_list[row+2][col-1-1*2**self.__left_arm(self.a,self.__root)-self.__loffset(row+2,col)+ self.__loffset(row,col)-8]=self.b
        if self.c is not None:
          self.vis_list[row+2][col+2+1*2**self.__right_arm(self.a,self.__root)-len(str(self.a))-self.__loffset(row+2,col)+self.__roffset(row,col)+8]=self.c
      elif self.j == self.get_height()-2 and self.__element_number>2**(self.get_height()-2) and self.get_height()>4:
        if self.b is not None:
          self.vis_list[row+2][col-1-1*2**self.__left_arm(self.a,self.__root)-self.__loffset(row+2,col)+ self.__loffset(row,col)-4]=self.b
        if self.c is not None:
          self.vis_list[row+2][col+2+1*2**self.__right_arm(self.a,self.__root)-len(str(self.a))-self.__loffset(row+2,col)+self.__roffset(row,col)+4]=self.c
      else:
        if self.b is not None:
          self.vis_list[row+2][col-1-1*2**self.__left_arm(self.a,self.__root)-self.__loffset(row+2,col)+ self.__loffset(row,col)]=self.b
        if self.c is not None:
          self.vis_list[row+2][col+2+1*2**self.__right_arm(self.a,self.__root)-len(str(self.a))-self.__loffset(row+2,col)+self.__roffset(row,col)]=self.c

  def __connection_drawer(self, row, col):
    if self.a is not None and self.a is not '_':
      if self.j == self.get_height()-1 and self.__element_number>2**(self.get_height()-2) and self.get_height()>4:
        if self.b is not None:
          self.vis_list[row+1][col-1*2**self.__left_arm(self.a,self.__root)+self.__loffset(row,col)-8]='/'
        if self.c is not None:
          self.vis_list[row+1][col+1*2**self.__right_arm(self.a,self.__root)+self.__roffset(row,col)+8]="\\"
      
      elif self.j == self.get_height()-2 and self.__element_number>2**(self.get_height()-2) and self.get_height()>4:
        if self.b is not None:
          self.vis_list[row+1][col-1*2**self.__left_arm(self.a,self.__root)+self.__loffset(row,col)-4]='/'
        if self.c is not None:
          self.vis_list[row+1][col+1*2**self.__right_arm(self.a,self.__root)+self.__roffset(row,col)+4]="\\"

      else:
        if self.b is not None:
          self.vis_list[row+1][col-1*2**self.__left_arm(self.a,self.__root)+self.__loffset(row,col)]='/'
        if self.c is not None:
          self.vis_list[row+1][col+1*2**self.__right_arm(self.a,self.__root)+self.__roffset(row,col)]="\\"

  def __loffset(self, row, col):
    a = 0
    for i in range(col):
      if self.vis_list[row][i] is not None and self.vis_list[row][i] is not '_':
        a += len(str(self.vis_list[row][i]))
        a -= 1
    return a

  def __roffset(self, row, col):
    a = 0
    for i in range(col+1):
      if self.vis_list[row][i] is not None and self.vis_list[row][i] is not '_':
        a += len(str(self.vis_list[row][i]))
        a -= 1
    return a

  def __list_creator(self):
    self.vis_list = [[None for i in range(100+2*2**self.get_height())] for j in range(2*self.get_height()-1)]
    self.vis_list[0][30+2**self.get_height()] = self.__root.value
    self.j = self.get_height()-1
    for i in range(0,2*self.get_height()-1,2):
      for j in range(0,100+2*2**self.get_height()):
        if self.vis_list[i][j] is not None and self.vis_list[i][j] is not '_':
          self.a = self.vis_list[i][j]
          self.b = self.__lvalue_loc(self.a,self.__root)
          self.c = self.__rvalue_loc(self.a,self.__root)
          self.__list_upd(i,j)
          self.__connection_drawer(i,j)
          self.__line_drawer(i,j)
      self.j -=1
  
  def __left_cutter(self):
    smallest = len(self.vis_list[0])
    for i in self.vis_list:
      j = 0
      while i[j] is None:
        j += 1
      if j < smallest:
        smallest = j
    return smallest

  def __right_cutter(self):
    largest = 0
    for i in self.vis_list:
      j = len(self.vis_list[0])-1
      while i[j] is None:
        j -= 1
      if j > largest:
        largest = j
    return largest     

  def visualize(self):
    self.__list_creator()
    self.visual_string = ''
    for i in self.vis_list:
      for v in range(self.__left_cutter()-1,self.__right_cutter()+1):
        if i[v] is None:
          self.visual_string += ' '
        else:
          self.visual_string += str(i[v])
      self.visual_string += '\n'
    return self.visual_string

  def __right_arm(self,value,position):
    if value>position.value:
      return self.__right_arm(value,position.right)
    elif value<position.value:
      return self.__right_arm(value,position.left)
    else:
      rightchild = position.right
      if rightchild.left is None:
        return 1
      else:
        return rightchild.left.height+1

  def __left_arm(self,value,position):
    if value>position.value:
      return self.__left_arm(value,position.right)
    elif value<position.value:
      return self.__left_arm(value,position.left)
    else:
      leftchild = position.left
      if leftchild.right is None:
        return 1
      else:
        return leftchild.right.height+1


# if __name__ == '__main__':
