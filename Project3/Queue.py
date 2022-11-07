from Deque_Generator import get_deque

class Queue:

  def __init__(self):
    # initialize a deque
    self.__dq = get_deque()

  def __str__(self):
    return str(self.__dq)

  def __len__(self):
    return len(self.__dq)

  # Enqueue from the back of the deque and dequeue from the front of the deque.
  # For a Queue with string representation [ 1, 2, 3 ], element 1 is the front and 3 is the back

  def enqueue(self, val):
    self.__dq.push_back(val)

  def dequeue(self):
    return self.__dq.pop_front()

  def peek(self):
    return self.__dq.peek_front()

  
