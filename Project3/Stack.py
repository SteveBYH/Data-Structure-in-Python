from Deque_Generator import get_deque

class Stack:

  def __init__(self):
    # initialize a deque
    self.__dq = get_deque()
    

  def __str__(self):
    return str(self.__dq)

  def __len__(self):
    return(len(self.__dq))

  # Here the top of the stack is chosen to be at the front position of the deque.
  # So both push and pop operations of stack uses deque functions for the front.
  # If a stack is [ 1, 2, 3 ], 1 is the top and 3 is the botton

  def push(self, val):
    self.__dq.push_front(val)

  def pop(self):
    return self.__dq.pop_front()

  def peek(self):
    return self.__dq.peek_front()

