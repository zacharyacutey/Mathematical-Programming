from NumberObject import Number
from __future__ import division
from sympy import re,im,Abs,floor,ceiling
MIN_N=-100
MAX_N=100
MIN_D=100
MAX_D=100
SET_OF_ALL={}
for i in range(MIN_V,MAX_V+1):
  for j in range(MIN_V,MAX_V+1):
    if not j==0:
      SET_OF_ALL.add(Number(i).Divide(j))
class Infinite:
  #Infinite paramteter takes local vars and returns a tuple consisting of (value,condition) {n:n+1} -> Infinite(lambda n : (n,n+1)
  def __init__(self,val):
    self.val=val
  @property
  def Type(self):
    return "Infinite"
  def Negative(self):
    raise TypeError
  def Not(self):
    raise TypeError
  def Positive(self):
    return Infinite(self.val)
  def Unpack(self):
    return self.Positive()
  def Complement(self):
    return Infinite(lambda n : (n,n.IsMemberOf(self).Not()))
  def RealPart(self):
    raise TypeError
  def ImaginaryPart(self):
    raise TypeError
  def Length(self):
    raise TypeError
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
      return Number(0)
    if arg.val==1:
      return self.Positive()
    raise TypeError
  def Divide(self,arg):
    if arg.val==1:
      return self.Positive()
    raise TypeError
  def Power(self,arg):
    if arg.val==0:
      return Number(1)
    if arg.val==1:
      return self.Positive()
    raise TypeError
  def Modulo(self,arg):
    raise TypeError
  def HasMember(self,arg):
    pass
    
