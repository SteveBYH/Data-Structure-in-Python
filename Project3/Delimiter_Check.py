import sys 
from Stack import Stack 

def delimiter_check(filename):
  left_delimiter = Stack()
  f = open(filename).read()
  for word in f.split():
    for letter in word:
      if letter == '(' or letter == '[' or letter == '{' :
        left_delimiter.push(letter)
      elif letter == ')':
        if left_delimiter.pop() == '(':
          pass
        else:
          return False
      elif letter == ']':
        if left_delimiter.pop() == '[':
          pass
        else:
          return False
      elif letter == '}':
        if left_delimiter.pop() == '{':
          pass
        else:
          return False
  return True

if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


