from __future__ import division
from NumberObject import NumberObject
print(u"αμπλ")
from sympy import re,im,Number,Abs,floor,ceiling
class FiniteSetObject:
  def __init__(self,*args):
    self.val=args
    i=0
    while i<len(self.val):
      j=i+1
      while j<len(self.val):
        if self.val[i].Equal(self.val[j]):
          self.val.pop(j)
        j=j+1
      i=i+1
  def Type(self):
    return "FiniteSet"
  def Negative(self):
    raise TypeError("You can not have a negative Set")
  def Not(self):
    raise TypeError("You can not do '~' to a Set")
  def Positive(self):
    return FiniteSetObject(*self.val)
  def Unpack(self):
    if len(self.val)==1:
      return self.val[0].Positive()
    return self.Positive()
  def Complement(self):
    return InfiniteSetObject(lambda n : self.HasMember(n).Not())
  def RealPart(self):
    raise TypeError("Cannot find real part of a set!")
  def ImaginaryPart(self):
    raise TypeError("Cannot find the imaginary part of a set!")
  def Length(self):
    return NumberObject(len(self.val))
  def Floor(self):
    raise TypeError("Cannot find the floor of a set!")
  def Ceiling(self):
    raise TypeError("Cannot find the ceiling of a set!")
  def AbsoluteValue(self):
    raise TypeError("Cannot find the absolute value of a set!")
  def Add(self,arg):
    if arg.val==0:
      return self.Positive()
    return self.Union(arg)
  def Minus(self,arg):
    if arg.val==0:
      return self.Positive()
    return self.SetDifference(arg)
  def Multiply(self,arg):
    if arg.val==0:
      return NumberObject(0)
    if arg.val==1:
      return self.Positive()
    raise TypeError("Cannot multiply a set")
  def Divide(self,arg):
    if arg.val==1:
      return self.Positive()
    raise TypeError("Cannot multiply sets")
  def Modulo(self,arg):
    raise TypeError("Cannot % sets")
  def Power(self,arg):
    if arg.val==0:
      return NumberObject(1)
    if arg.val==1:
      return self.Positive()
    raise TypeError("Cannot Exponentiate sets")
class InfiniteSetObject:
  pass
