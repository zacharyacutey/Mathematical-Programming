from __future__ import division
from sympy import floor,ceiling,Abs,re,im
from NumberObject import Number
class Function:
  def __init__(self,val):
    self.val=val
  @property
  def Type(self):
    return "Function"
  def Negative(self):
    raise TypeError
  def Not(self):
    raise TypeError
  def Positive(self):
    return Function(self.val)
  def Unpack(self):
    return self.Positive()
  def Complement(self):
    raise TypeError
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
    raise TypeError
  def Minus(self,arg):
    raise TypeError
  def Multiply(self,arg):
    raise TypeError
  def Divide(self,arg):
    raise TypeError
  def Modulo(self,arg):
    raise TypeError
  def Power(self,arg):
    raise TypeError
  def HasMember(self,arg):
    raise TypeError
  def IsMemberOf(self,arg):
    raise TypeError
