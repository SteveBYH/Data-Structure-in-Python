import time
from Stack import Stack

def Hanoi_rec(n, s, a, d):
  print(n, s, a, d)
  if n == 0:
    # place the only piece into destination
    d.push(s.pop())
  else:
    # place the first n-1 piece to the aux
    Hanoi_rec(n-1,s,d,a)
    # place the largest piece to desination
    d.push(s.pop())
    # place the remaining n-1 piece from aux to destination
    Hanoi_rec(n-1,a,s,d)
  print(n, s, a, d)
  print()

def Hanoi(n):
  source = Stack()
  dest = Stack()
  aux = Stack()
  i = n-1
  while i >= 0:
    source.push(i)
    i = i - 1
  Hanoi_rec(n-1, source, aux, dest)

if __name__ == '__main__':
  start = time.clock()
  n = 8
  Hanoi(n)
  end = time.clock()
  print('computed Hanoi(' + str(n) + ') in ' + str(end - start) + ' seconds.')
