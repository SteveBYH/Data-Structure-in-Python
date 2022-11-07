from random import shuffle
from Binary_Search_Tree import Binary_Search_Tree
class Fraction:

  def __init__(self, numerator, denominator):
    # use caution here... In most languages, it is not a good idea to
    # raise an exception from a constructor. Python is a bit different
    # and it shouldn't cause a problem here.
    if denominator == 0:
      raise ZeroDivisionError
    self.__n = numerator
    self.__d = denominator
    self.__reduce()

  @staticmethod
  def gcd(n, d):
    while d != 0:
      t = d
      d = n % d
      n = t
    return n

  def __reduce(self):
    if self.__n < 0 and self.__d < 0:
      self.__n = self.__n * -1
      self.__d = self.__d * -1

    divisor = Fraction.gcd(self.__n, self.__d)
    self.__n = self.__n // divisor
    self.__d = self.__d // divisor

  def __add__(self, addend):
    num = self.__n * addend.__d + self.__d * addend.__n
    den = self.__d * addend.__d
    return Fraction(num, den)

  def __sub__(self, subtrahend):
    num = self.__n * subtrahend.__d - self.__d * subtrahend.__n
    den = self.__d * subtrahend.__d
    return Fraction(num, den)

  def __mul__(self, multiplicand):
    num = self.__n * multiplicand.__n
    den = self.__d * multiplicand.__d
    return Fraction(num, den)

  def __truediv__(self, divisor):
    if divisor.__n == 0:
      raise ZeroDivisionError
    num = self.__n * divisor.__d
    den = self.__d * divisor.__n
    return Fraction(num, den)

  def __lt__(self, other):
    # subtract other from the current fraction self
    dif = self.__sub__(other)
    # if self < other, self - other < 0
    # denominator and numerator should have opposite sign
    if dif.__n * dif.__d < 0:
      return True
    else:
      return False

  def __gt__(self, other):
    # subtract other from the current fraction self
    dif = self.__sub__(other)
    # if self < other, self - other < 0
    # denominator and numerator should have same sign 
    if dif.__n * dif.__d > 0:
      return True
    else:
      return False 
    

  def __eq__(self, other):
    # subtract other from the current fraction self
    dif = self.__sub__(other)
    # if self < other, self - other < 0
    # numerator should be 0
    if dif.__n == 0:
      return True
    else:
      return False 
    

  def to_float(self):
    #this is safe because we don't allow a
    #zero denominator
    return self.__n / self.__d

  def __str__(self):
    return str(self.__n) + '/' + str(self.__d)

  # the __repr__ method is similar to __str__, but is called
  # when Python wants to display these objects in a container like
  # a Python list.
  def __repr__(self):
    return str(self)

if __name__ == '__main__':
  k = Binary_Search_Tree()
  # Create numerators
  a = [i for i in range (-1000,1000)]
  # Randomize numerators
  shuffle(a)
  # Create the list of Fractions
  c = [Fraction(q,120) for q in a]
  # Insert into the AVL Tree
  for i in c:
    k.insert_element(i)
  print(c)
  print(k.to_list())
    
