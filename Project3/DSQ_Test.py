import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()


# First test the deque which is the basis for stack and queue

  def test_empty_deque_string(self):
    self.assertEqual('[ ]', str(self.__deque))

  # Test the push_front function

  def test_push_front_empty(self):
    self.__deque.push_front(1)
    self.assertEqual('[ 1 ]', str(self.__deque))
  
  def test_push_front_with_one(self):
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.assertEqual('[ 1, 2 ]', str(self.__deque))

  def test_push_front_with_two(self):
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.assertEqual('[ 1, 2, 3 ]', str(self.__deque))

  def test_push_front_with_three(self):
    self.__deque.push_front(4)
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.assertEqual('[ 1, 2, 3, 4 ]', str(self.__deque))

  # Test the len function
  def test_len_empty(self):
    self.assertEqual(0, len(self.__deque))

  def test_len_with_one(self):
    self.__deque.push_front(1)
    self.assertEqual(1, len(self.__deque))
  
  def test_len_with_two(self):
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.assertEqual(2, len(self.__deque))

  def test_len_with_three(self):
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.assertEqual(3, len(self.__deque))

  def test_len_with_four(self):
    self.__deque.push_front(4)
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.assertEqual(4, len(self.__deque))

  # Test the push_back function
  # Should add one to the deque and implement size by 1

  def test_push_back_empty(self):
    self.__deque.push_back(1)
    self.assertEqual('[ 1 ]', str(self.__deque))

  def test_len_after_push_back_empty(self):
    self.__deque.push_back(1)
    self.assertEqual(1, len(self.__deque))
  
  def test_push_back_with_one(self):
    self.__deque.push_back(1)
    self.__deque.push_back(2)
    self.assertEqual('[ 1, 2 ]', str(self.__deque))

  def test_len_after_push_back_with_one(self):
    self.__deque.push_back(1)
    self.__deque.push_back(2)
    self.assertEqual(2, len(self.__deque))

  def test_push_back_with_two(self):
    self.__deque.push_back(1)
    self.__deque.push_back(2)
    self.__deque.push_back(3)
    self.assertEqual('[ 1, 2, 3 ]', str(self.__deque))

  def test_len_after_push_back_with_two(self):
    self.__deque.push_back(1)
    self.__deque.push_back(2)
    self.__deque.push_back(3)
    self.assertEqual(3, len(self.__deque))

  def test_push_back_with_three(self):
    self.__deque.push_back(1)
    self.__deque.push_back(2)
    self.__deque.push_back(3)
    self.__deque.push_back(4)
    self.assertEqual('[ 1, 2, 3, 4 ]', str(self.__deque))
  
  def test_len_after_push_back_with_three(self):
    self.__deque.push_back(1)
    self.__deque.push_back(2)
    self.__deque.push_back(3)
    self.__deque.push_back(4)
    self.assertEqual(4, len(self.__deque))
  
  # Test the peek_front function
  # Should return the front value without changing the deque
  def test_peek_front_empty(self):
    self.assertEqual(None, self.__deque.peek_front())

  def test_remaining_after_peek_front_empty(self):
    self.__deque.peek_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_len_after_peek_front_empty(self):
    self.__deque.peek_front()
    self.assertEqual(0, len(self.__deque))

  def test_peek_front_with_one(self):
    self.__deque.push_front(1)
    self.assertEqual(1, self.__deque.peek_front())
  
  def test_remaining_after_peek_front_with_one(self):
    self.__deque.push_front(1)
    self.__deque.peek_front()
    self.assertEqual('[ 1 ]',str(self.__deque))

  def test_len_after_peek_front_with_one(self):
    self.__deque.push_front(1)
    self.__deque.peek_front()
    self.assertEqual(1, len(self.__deque))
  
  def test_peek_front_with_two(self):
    self.__deque.push_front(1)
    self.__deque.push_back(2)
    self.assertEqual(1, self.__deque.peek_front())

  def test_remaining_after_peek_front_with_two(self):
    self.__deque.push_front(2)
    self.__deque.push_back(1)
    self.__deque.pop_back()
    self.__deque.pop_back()
    self.__deque.push_front(1)
    self.__deque.push_back(2)
    self.__deque.peek_front()
    self.assertEqual('[ 1, 2 ]',str(self.__deque))

  def test_len_after_peek_front_with_two(self):
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.__deque.peek_front()
    self.assertEqual(2, len(self.__deque))

  def test_peek_front_with_three(self):
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.assertEqual(1, self.__deque.peek_front())

  def test_remaining_after_peek_front_with_three(self):
    # add some permutation of push and pop functions
    # test whether there exists hidden errors
    self.__deque.push_front(3)
    self.__deque.push_front(3)
    self.__deque.pop_back()
    self.__deque.pop_front()
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.__deque.peek_front()
    self.assertEqual('[ 1, 2, 3 ]',str(self.__deque))

  def test_len_after_peek_front_with_three(self):
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.__deque.peek_front()
    self.assertEqual(3, len(self.__deque))

  def test_peek_front_with_four(self):
    self.__deque.push_front(4)
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.assertEqual(1, self.__deque.peek_front())

  def test_remaining_after_peek_front_with_four(self):
    self.__deque.push_front(4)
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.__deque.peek_front()
    self.assertEqual('[ 1, 2, 3, 4 ]',str(self.__deque))

  def test_len_after_peek_front_with_four(self):
    self.__deque.push_front(4)
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.__deque.peek_front()
    self.assertEqual(4, len(self.__deque))

  # Test the peek_back function
  # Should return the back value without changing the deque

  def test_peek_back_empty(self):
    self.assertEqual(None, self.__deque.peek_back())

  def test_string_after_peek_back_empty(self):
    self.__deque.peek_back()
    self.assertEqual('[ ]',str(self.__deque))
  
  def test_len_after_peek_back_empty(self):
    self.__deque.peek_back()
    self.assertEqual(0, len(self.__deque))

  def test_peek_back_with_one(self):
    self.__deque.push_front(1)
    self.assertEqual(1, self.__deque.peek_back())
  
  def test_string_after_peek_back_with_one(self):
    self.__deque.push_front(1)
    self.__deque.peek_back()
    self.assertEqual('[ 1 ]',str(self.__deque))

  def test_len_after_peek_back_with_one(self):
    self.__deque.push_back(1)
    self.__deque.peek_back()
    self.assertEqual(1, len(self.__deque))
  
  def test_peek_back_with_two(self):
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.assertEqual(2, self.__deque.peek_back())

  def test_string_after_peek_back_with_two(self):
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.__deque.peek_back()
    self.assertEqual('[ 1, 2 ]',str(self.__deque))

  def test_len_after_peek_back_with_two(self):
    self.__deque.push_back(2)
    self.__deque.push_back(1)
    self.__deque.peek_back()
    self.assertEqual(2, len(self.__deque))

  def test_peek_back_with_three(self):
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.assertEqual(3, self.__deque.peek_back())

  def test_string_after_peek_back_with_three(self):
    # add some permutation of pop and push function 
    # test whether there are hidden error
    self.__deque.push_front(310)
    self.__deque.push_back(3)
    self.__deque.push_front(2)
    self.__deque.push_back(3)
    self.__deque.push_front(0)
    self.__deque.pop_back()
    self.__deque.pop_front()
    self.__deque.pop_back()
    self.__deque.pop_front()
    self.__deque.pop_back()
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.__deque.peek_back()
    self.assertEqual('[ 1, 2, 3 ]',str(self.__deque))

  def test_len_after_peek_back_with_three(self):
    self.__deque.push_back(3)
    self.__deque.push_back(2)
    self.__deque.push_back(1)
    self.__deque.peek_back()
    self.assertEqual(3, len(self.__deque))

  def test_peek_back_with_four(self):
    self.__deque.push_front(4)
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.assertEqual(4, self.__deque.peek_back())

  def test_string_after_peek_back_with_four(self):
    self.__deque.push_front(4)
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.__deque.peek_back()
    self.assertEqual('[ 1, 2, 3, 4 ]',str(self.__deque))

  def test_len_after_peek_back_with_four(self):
    self.__deque.push_back(4)
    self.__deque.push_back(3)
    self.__deque.push_back(2)
    self.__deque.push_back(1)
    self.__deque.peek_back()
    self.assertEqual(4, len(self.__deque))

  # Test the pop_front funtion
  # Should pop and return the front value, decrease the size by 1

  def test_pop_front_empty(self):
    self.assertEqual(None, self.__deque.pop_front())

  def test_string_after_pop_front_empty(self):
    self.__deque.pop_front()
    self.assertEqual('[ ]',str(self.__deque))

  def test_len_after_pop_front_empty(self):
    self.__deque.pop_front()
    self.assertEqual(0,len(self.__deque))

  def test_pop_front_with_one(self):
    self.__deque.push_front(1)
    self.assertEqual(1, self.__deque.pop_front())
  
  def test_string_after_pop_front_with_one(self):
    self.__deque.push_front(1)
    self.__deque.pop_front()
    self.assertEqual('[ ]',str(self.__deque))
  
  def test_len_after_pop_front_with_one(self):
    self.__deque.push_front(1)
    self.__deque.pop_front()
    self.assertEqual(0,len(self.__deque))
  
  def test_pop_front_with_two(self):
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.assertEqual(1, self.__deque.pop_front())

  def test_string_after_pop_front_with_two(self):
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.__deque.pop_front()
    self.assertEqual('[ 2 ]',str(self.__deque))

  def test_len_after_pop_front_with_two(self):
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.__deque.pop_front()
    self.assertEqual(1,len(self.__deque))

  def test_pop_front_with_three(self):
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.assertEqual(1, self.__deque.pop_front())

  def test_string_after_pop_front_with_three(self):
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.__deque.pop_front()
    self.assertEqual('[ 2, 3 ]',str(self.__deque))

  def test_len_after_pop_front_with_three(self):
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.__deque.pop_front()
    self.assertEqual(2,len(self.__deque))

  def test_pop_front_with_four(self):
    self.__deque.push_front(4)
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.assertEqual(1, self.__deque.pop_front())

  def test_string_after_pop_front_with_four(self):
    self.__deque.push_front(4)
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.__deque.pop_front()
    self.assertEqual('[ 2, 3, 4 ]',str(self.__deque))

  def test_len_after_pop_front_with_four(self):
    self.__deque.push_front(4)
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.__deque.pop_front()
    self.assertEqual(3,len(self.__deque))

  # Test the pop_back funtion
  # Should pop and return the back value, decrease the size by 1

  def test_pop_back_empty(self):
    self.assertEqual(None, self.__deque.pop_back())

  def test_string_after_pop_back_empty(self):
    self.__deque.pop_back()
    self.assertEqual('[ ]',str(self.__deque))

  def test_len_after_pop_back_empty(self):
    self.__deque.pop_back()
    self.assertEqual(0,len(self.__deque))

  def test_pop_back_with_one(self):
    self.__deque.push_front(1)
    self.assertEqual(1, self.__deque.pop_back())
  
  def test_string_after_pop_back_with_one(self):
    self.__deque.push_front(1)
    self.__deque.pop_back()
    self.assertEqual('[ ]',str(self.__deque))
  
  def test_len_after_pop_back_with_one(self):
    self.__deque.push_front(1)
    self.__deque.pop_back()
    self.assertEqual(0,len(self.__deque))
  
  def test_pop_back_with_two(self):
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.assertEqual(2, self.__deque.pop_back())

  def test_string_after_pop_back_with_two(self):
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.__deque.pop_back()
    self.assertEqual('[ 1 ]',str(self.__deque))

  def test_len_after_pop_back_with_two(self):
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.__deque.pop_back()
    self.assertEqual(1,len(self.__deque))

  def test_pop_back_with_three(self):
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.assertEqual(3, self.__deque.pop_back())

  def test_string_after_pop_back_with_three(self):
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.__deque.pop_back()
    self.assertEqual('[ 1, 2 ]',str(self.__deque))

  def test_len_after_pop_back_with_three(self):
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.__deque.pop_back()
    self.assertEqual(2,len(self.__deque))

  def test_pop_back_with_four(self):
    self.__deque.push_front(4)
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.assertEqual(4, self.__deque.pop_back())

  def test_string_after_pop_back_with_four(self):
    self.__deque.push_front(4)
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.__deque.pop_back()
    self.assertEqual('[ 1, 2, 3 ]',str(self.__deque))

  def test_len_after_pop_back_with_four(self):
    self.__deque.push_front(4)
    self.__deque.push_front(3)
    self.__deque.push_front(2)
    self.__deque.push_front(1)
    self.__deque.pop_back()
    self.assertEqual(3,len(self.__deque))



# Then test the Stack Class

  def test_stack_string_empty(self):
    self.assertEqual('[ ]', str(self.__stack))

  # Test the push function:
  def test_stack_push_empty(self):
    self.__stack.push(1)
    self.assertEqual('[ 1 ]', str(self.__stack))

  def test_stack_push_with_one(self):
    self.__stack.push(2)
    self.__stack.push(1)
    self.assertEqual('[ 1, 2 ]', str(self.__stack))

  def test_stack_push_with_two(self):
    self.__stack.push(3)
    self.__stack.push(2)
    self.__stack.push(1)
    self.assertEqual('[ 1, 2, 3 ]', str(self.__stack))

  def test_stack_push_with_three(self):
    self.__stack.push(4)
    self.__stack.push(3)
    self.__stack.push(2)
    self.__stack.push(1)
    self.assertEqual('[ 1, 2, 3, 4 ]', str(self.__stack))

  # Test the len function

  def test_stack_len_empty(self):
    self.assertEqual(0, len(self.__stack))

  def test_stack_len_with_one(self):
    self.__stack.push(1)
    self.assertEqual(1, len(self.__stack))

  def test_stack_len_with_two(self):
    self.__stack.push(2)
    self.__stack.push(1)
    self.assertEqual(2, len(self.__stack))

  def test_stack_len_with_three(self):
    self.__stack.push(3)
    self.__stack.push(2)
    self.__stack.push(1)
    self.assertEqual(3, len(self.__stack))

  # Test the peek function
  # The peek function should return the top value leaving the stack unchanged

  def test_stack_peek_empty(self):
    self.assertEqual(None, self.__stack.peek())

  def test_remaining_stack_after_peek_empty(self):
    self.__stack.peek()
    self.assertEqual('[ ]', str(self.__stack))

  def test_stack_len_after_peek_empty(self):
    self.__stack.peek()
    self.assertEqual(0, len(self.__stack))

  def test_stack_peek_with_one(self):
    self.__stack.push(1)
    self.assertEqual(1, self.__stack.peek())

  def test_remaining_stack_after_peek_with_one(self):
    self.__stack.push(1)
    self.__stack.peek()
    self.assertEqual('[ 1 ]', str(self.__stack))

  def test_stack_len_after_peek_with_one(self):
    self.__stack.push(1)
    self.__stack.peek()
    self.assertEqual(1, len(self.__stack))

  def test_stack_peek_with_two(self):
    self.__stack.push(2)
    self.__stack.push(1)
    self.assertEqual(1, self.__stack.peek())

  def test_remaining_stack_after_peek_with_two(self):
    # various permutations are added to avoid hidden error
    self.__stack.push(20)
    self.__stack.push(38)
    self.__stack.pop()
    self.__stack.push(2)
    self.__stack.push(2)
    self.__stack.pop()
    self.__stack.push(2)
    self.__stack.pop()
    self.__stack.pop()
    self.__stack.pop()
    self.__stack.push(2)
    self.__stack.push(1)
    self.__stack.peek()
    self.assertEqual('[ 1, 2 ]', str(self.__stack))

  def test_stack_len_after_peek_with_two(self):
    self.__stack.push(2)
    self.__stack.push(1)
    self.__stack.peek()
    self.assertEqual(2, len(self.__stack))

  def test_stack_peek_with_three(self):
    self.__stack.push(3)
    self.__stack.push(2)
    self.__stack.push(1)
    self.assertEqual(1, self.__stack.peek())

  def test_remaining_stack_after_peek_with_three(self):
    self.__stack.push(3)
    self.__stack.push(2)
    self.__stack.push(1)
    self.__stack.peek()
    self.assertEqual('[ 1, 2, 3 ]', str(self.__stack))

  def test_stack_len_after_peek_with_three(self):
    self.__stack.push(3)
    self.__stack.push(2)
    self.__stack.push(1)
    self.__stack.peek()
    self.assertEqual(3, len(self.__stack))

  # Test the pop function
  # Should pop and return the top value and decrease the size by 1
  def test_stack_pop_empty(self):
    self.assertEqual(None, self.__stack.pop())

  def test_stack_remaining_after_pop_empty(self):
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))

  def test_stack_len_after_pop_empty(self):
    self.__stack.pop()
    self.assertEqual(0, len(self.__stack))

  def test_stack_pop_with_one(self):
    self.__stack.push(1)
    self.assertEqual(1, self.__stack.pop())

  def test_stack_remaining_after_with_one(self):
    self.__stack.push(1)
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))

  def test_stack_len_after_pop_with_one(self):
    self.__stack.push(1)
    self.__stack.pop()
    self.assertEqual(0, len(self.__stack))

  def test_stack_pop_with_two(self):
    self.__stack.push(2)
    self.__stack.push(1)
    self.assertEqual(1, self.__stack.pop())

  def test_stack_remaining_after_with_two(self):
    self.__stack.push(2)
    self.__stack.push(1)
    self.__stack.pop()
    self.assertEqual('[ 2 ]', str(self.__stack))

  def test_stack_len_after_pop_with_two(self):
    self.__stack.push(2)
    self.__stack.push(1)
    self.__stack.pop()
    self.assertEqual(1, len(self.__stack))

  def test_stack_pop_with_three(self):
    self.__stack.push(3)
    self.__stack.push(2)
    self.__stack.push(1)
    self.assertEqual(1, self.__stack.pop())

  def test_stack_remaining_after_with_three(self):
    self.__stack.push(3)
    self.__stack.push(2)
    self.__stack.push(1)
    self.__stack.pop()
    self.assertEqual('[ 2, 3 ]', str(self.__stack))

  def test_stack_len_after_pop_with_three(self):
    self.__stack.push(3)
    self.__stack.push(2)
    self.__stack.push(1)
    self.__stack.pop()
    self.assertEqual(2, len(self.__stack))

  def test_stack_pop_with_four(self):
    self.__stack.push(4)
    self.__stack.push(3)
    self.__stack.push(2)
    self.__stack.push(1)
    self.assertEqual(1, self.__stack.pop())

  def test_stack_remaining_after_with_four(self):
    self.__stack.push(4)
    self.__stack.push(3)
    self.__stack.push(2)
    self.__stack.push(1)
    self.__stack.pop()
    self.assertEqual('[ 2, 3, 4 ]', str(self.__stack))

  def test_stack_len_after_pop_with_four(self):
    self.__stack.push(4)
    self.__stack.push(3)
    self.__stack.push(2)
    self.__stack.push(1)
    self.__stack.pop()
    self.assertEqual(3, len(self.__stack))


# Then test the Queue Class

  def test_queue_string_empty(self):
    self.assertEqual('[ ]', str(self.__queue))

  # Test the enqueue function:
  def test_queue_enqueue_empty(self):
    self.__queue.enqueue(1)
    self.assertEqual('[ 1 ]', str(self.__queue))

  def test_queue_enqueue_with_one(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.assertEqual('[ 1, 2 ]', str(self.__queue))

  def test_queue_enqueue_with_two(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.enqueue(3)
    self.assertEqual('[ 1, 2, 3 ]', str(self.__queue))

  def test_queue_enqueue_with_three(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.enqueue(3)
    self.__queue.enqueue(4)
    self.assertEqual('[ 1, 2, 3, 4 ]', str(self.__queue))

  # Test the len function
  def test_queue_len_empty(self):
    self.assertEqual(0, len(self.__queue))

  def test_queue_len_with_one(self):
    self.__queue.enqueue(1)
    self.assertEqual(1, len(self.__queue))

  def test_queue_len_with_two(self):
    self.__queue.enqueue(2)
    self.__queue.enqueue(1)
    self.assertEqual(2, len(self.__queue))

  def test_queue_len_with_three(self):
    self.__queue.enqueue(3)
    self.__queue.enqueue(2)
    self.__queue.enqueue(1)
    self.assertEqual(3, len(self.__queue))

  # Test the peek function
  # The peek function should return the top value leaving the queue unchanged

  def test_queue_peek_empty(self):
    self.assertEqual(None, self.__queue.peek())

  def test_remaining_queue_after_peek_empty(self):
    self.__queue.peek()
    self.assertEqual('[ ]', str(self.__queue))

  def test_queue_len_after_peek_empty(self):
    self.__queue.peek()
    self.assertEqual(0, len(self.__queue))

  def test_queue_peek_with_one(self):
    self.__queue.enqueue(1)
    self.assertEqual(1, self.__queue.peek())

  def test_remaining_queue_after_peek_with_one(self):
    self.__queue.enqueue(1)
    self.__queue.peek()
    self.assertEqual('[ 1 ]', str(self.__queue))
  
  def test_queue_len_after_peek_with_one(self):
    self.__queue.enqueue(1)
    self.__queue.peek()
    self.assertEqual(1, len(self.__queue))

  def test_queue_peek_with_two(self):
    self.__queue.enqueue(2)
    self.__queue.enqueue(1)
    self.assertEqual(2, self.__queue.peek())

  def test_remaining_queue_after_peek_with_two(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.peek()
    self.assertEqual('[ 1, 2 ]', str(self.__queue))

  def test_queue_len_after_peek_with_two(self):
    self.__queue.enqueue(2)
    self.__queue.enqueue(1)
    self.__queue.peek()
    self.assertEqual(2, len(self.__queue))

  def test_queue_peek_with_three(self):
    self.__queue.enqueue(3)
    self.__queue.enqueue(2)
    self.__queue.enqueue(1)
    self.assertEqual(3, self.__queue.peek())

  def test_remaining_queue_after_peek_with_three(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.enqueue(3)
    self.__queue.peek()
    self.assertEqual('[ 1, 2, 3 ]', str(self.__queue))

  def test_queue_len_after_peek_with_three(self):
    self.__queue.enqueue(3)
    self.__queue.enqueue(2)
    self.__queue.enqueue(1)
    self.__queue.peek()
    self.assertEqual(3, len(self.__queue))

  # Test the pop function
  # Should pop and return the top value and decrease the size by 1
  def test_queue_dequeue_empty(self):
    self.assertEqual(None, self.__queue.dequeue())

  def test_queue_remaining_after_dequeue_empty(self):
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))

  def test_queue_len_after_dequeue_empty(self):
    self.__queue.dequeue()
    self.assertEqual(0, len(self.__queue))

  def test_queue_dequeue_with_one(self):
    self.__queue.enqueue(1)
    self.assertEqual(1, self.__queue.dequeue())

  def test_queue_remaining_after_with_one(self):
    self.__queue.enqueue(1)
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))

  def test_queue_len_after_dequeue_with_one(self):
    self.__queue.enqueue(1)
    self.__queue.dequeue()
    self.assertEqual(0, len(self.__queue))

  def test_queue_dequeue_with_two(self):
    self.__queue.enqueue(2)
    self.__queue.enqueue(1)
    self.assertEqual(2, self.__queue.dequeue())

  def test_queue_remaining_after_with_two(self):
    self.__queue.enqueue(2)
    self.__queue.enqueue(1)
    self.__queue.dequeue()
    self.assertEqual('[ 1 ]', str(self.__queue))

  def test_queue_len_after_dequeue_with_two(self):
    self.__queue.enqueue(2)
    self.__queue.enqueue(1)
    self.__queue.dequeue()
    self.assertEqual(1, len(self.__queue))

  def test_queue_dequeue_with_three(self):
    self.__queue.enqueue(3)
    self.__queue.enqueue(2)
    self.__queue.enqueue(1)
    self.assertEqual(3, self.__queue.dequeue())

  def test_queue_remaining_after_with_three(self):
    self.__queue.enqueue(3)
    self.__queue.enqueue(2)
    self.__queue.enqueue(1)
    self.__queue.dequeue()
    self.assertEqual('[ 2, 1 ]', str(self.__queue))

  def test_queue_len_after_dequeue_with_three(self):
    self.__queue.enqueue(3)
    self.__queue.enqueue(2)
    self.__queue.enqueue(1)
    self.__queue.dequeue()
    self.assertEqual(2, len(self.__queue))

  def test_queue_dequeue_with_four(self):
    self.__queue.enqueue(4)
    self.__queue.enqueue(3)
    self.__queue.enqueue(2)
    self.__queue.enqueue(1)
    self.assertEqual(4, self.__queue.dequeue())

  def test_queue_remaining_after_with_four(self):
    # various permutations are added to avoid hidden error
    self.__queue.enqueue(4)
    self.__queue.dequeue()
    self.__queue.enqueue(4)
    self.__queue.enqueue(4)
    self.__queue.enqueue(4)
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.__queue.enqueue(4)
    self.__queue.enqueue(4)
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.__queue.enqueue(4)
    self.__queue.dequeue()
    self.__queue.enqueue(3)
    self.__queue.enqueue(2)
    self.__queue.enqueue(1)
    self.__queue.dequeue()
    self.assertEqual('[ 3, 2, 1 ]', str(self.__queue))

  def test_queue_len_after_dequeue_with_four(self):
    self.__queue.enqueue(4)
    self.__queue.enqueue(3)
    self.__queue.enqueue(2)
    self.__queue.enqueue(1)
    self.__queue.dequeue()
    self.assertEqual(3, len(self.__queue))


if __name__ == '__main__':
  unittest.main()

