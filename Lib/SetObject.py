from __future__ import division
from NumberObject import NumberObject
print(u"αμπλ")
from sympy import re,im,Number,Abs,floor,ceiling
class FiniteSetObject:
  def __init__(self,*args):
    for i of args:
      if i.Type()!="SetF" and i.Type()!="Number":
        raise TypeError
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
    return "SetF"
  def Negative(self):
    raise TypeError
  def Not(self):
    raise TypeError
  def Positive(self):
    return FiniteSetObject(*self.val)
  def Unpack(self):
    if len(self.val)==1:
      return self.val[0].Positive()
    return self.Positive()
  def Complement(self):
    return InfiniteSetObject(lambda n : self.HasMember(n).Not())
  def RealPart(self):
    raise TypeError
  def ImaginaryPart(self):
    raise TypeError
  def Length(self):
    return NumberObject(len(self.val))
  def Floor(self):
    raise TypeError
  def Ceiling(self):
    raise TypeError
  def AbsoluteValue(self):
    raise TypeError
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
    raise TypeError
  def Divide(self,arg):
    if arg.val==1:
      return self.Positive()
    raise TypeError
  def Modulo(self,arg):
    raise TypeError
  def Power(self,arg):
    if arg.val==0:
      return NumberObject(1)
    if arg.val==1:
      return self.Positive()
    raise TypeError
class InfiniteSetObject:
  pass
