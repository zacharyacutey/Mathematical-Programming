#Requires sympy and any of its dependencies
from __future__ import division
try:
  from sympy import re,im,Number,Abs,floor,ceiling
except ImportError:
  raise RuntimeError("You must install sympy and any of its dependencies")
  exit()
class NumberObject:
  def __init__(self,val):
    self.val=Number(val)
  def Type(self):
    return "Number"
  def Negative(self):
    return NumberObject(-self.val)
  def Not(self):
    return NumberObject(1 if self.val==0 else 0)
  def Positive(self):
    return NumberObject(self.val)
  def Unpack(self):
    return NumberObject(self.val)
  def Complement(self):
    raise TypeError("You can not complement a number!")
  def RealPart(self):
    return NumberObject(re(self.val))
  def ImaginaryPart(self):
    return NumberObject(im(self.val))
  def Length(self):
    return NumberObject(0)
  def Floor(self):
    return NumberObject(floor(self.val))
  def Ceiling(self):
    return NumberObject(ceiling(self.val))
  def AbsoluteValue(self):
    return NumberObject(Abs(self.val))
  def Add(self,arg):
    if self.val==0:
      return arg.Positive()
    if arg.val==0:
      return self.Positive()
    return NumberObject(self.val+arg.val)
  def Minus(self,arg):
    if self.val==0:
      return arg.Negative()
    if arg.val==0:
      return self.Positive()
    if self.val==arg.val:
      return NumberObject(0)
    return NumberObject(self.val-arg.val)
  def Multiply(self,arg):
    if self.val==0:
      return NumberObject(0)
    if arg.val==0:
      return NumberObject(0)
    if self.val==1:
      return arg.Positive()
    if arg.val==1:
      return self.Positive()
    if arg.val==-1:
      return self.Negative()
    if self.val==-1:
      return arg.Negative()
    return NumberObject(self.val*arg.val)
  def Divide(self,arg):
    if arg.val==0:
      raise DivideByZeroError("The second argument cannot be 0")
    if arg.val==1:
      return self.Positive()
    if arg.val==-1:
      return self.Negative()
    if self.val==arg.val:
      return NumberObject(1)
    if self.val==arg.Negative().val:
      return NumberObject(-1)
    if self.val==0:
      return NumberObject(0)
    return NumberObject(self.val/arg.val)
  def Modulo(self,arg):
    return self.Minus(arg.Multiply(self.Divide(arg).Floor()))
  def Power(self,arg):
    if arg.val==0:
      return NumberObject(1)
    if self.val==0:
      return NumberObject(0)
    if arg.val==1:
      return self.Positive()
    if self.val==1:
      return NumberObject(1)
    if arg.val==-1:
      return NumberObject(1).Divide(self)
    return NumberObject(self.val**arg.val)
  
