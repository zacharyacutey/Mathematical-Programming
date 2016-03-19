from __future__ import division
from sympy import floor,ceiling,Abs,re,im
from NumberObject import Number
from InfiniteObject import SET_OF_ALL,DoSomething
#To do: implement conditions of numbers that have a definite evaluation
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
    if arg.val==0:
      return self.Positive()
    raise TypeError
  def Minus(self,arg):
    if arg.val==0:
      raise self.Positive()
    raise TypeError
  def Multiply(self,arg):
    if arg.val==0:
      return Number(0)
    if arg.val==1:
      return self.Positive()
    raise TypeError
  def Divide(self,arg):
    if arg.val==0:
      raise DivideByZeroError
    if arg.val==1:
      return self.Positive()
    raise TypeError
  def Modulo(self,arg):
    raise TypeError
  def Power(self,arg):
    if arg.val==0:
      return Number(1)
    if arg.val==1:
      return self.Positive()
    raise TypeError
  def HasMember(self,arg):
    raise TypeError
  def IsMemberOf(self,arg):
    raise TypeError
  def And(self,arg):
    raise TypeError
  def Or(self,arg):
    raise TypeError
  def Intersection(self,arg):
    raise TypeError
  def Union(self,arg):
    raise TypeError
  def SetDifference(self,arg):
    raise TypeError
  def Less(self,arg):
    raise TypeError
  def LessEqual(self,arg):
    raise TypeError
  def Greater(self,arg):
    raise TypeError
  def GreaterEqual(self,arg):
    raise TypeError
  def Equal(self,arg):
    return Number(0)
  def NotEqual(self,arg):
    return Number(1)
  def Subset(self,arg):
    raise TypeError
  def SubsetEqual(self,arg):
    raise TypeError
  def Superset(self,arg):
    raise TypeError
  def SupersetEqual(self,arg):
    raise TypeError
  def SetEqual(self,arg):
    raise TypeError
  def SetNotEqual(self,arg):
    raise TypeError
  def IfThenElse(self,first,last):
    raise TypeError
  def Call(self,*args):
    return self.val(*args)
  def InfiniteSum(self):
    r=Number(0)
    for i in DoSomething(1):
      r=r.Add(self.val(i))
    return r
  def InfiniteProduct(self):
    r=Number(1)
    for i in DoSomething(1):
      r=r.Multiply(self.val(i))
    return r
  def __str__(self):
    return "Function("+str(self.val)+")"
