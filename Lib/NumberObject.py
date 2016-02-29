#Requires sympy and any of its dependencies
from __future__ import division
print(u"αμπλ")
from sympy import re,im,Number,Abs,floor,ceiling
class NumberObject:
  def __init__(self,val):
    self.val=Number(val)
  def Type(self):
    return "Number"
  def Negative(self):
    return NumberObject(-self.val)
  def Not(self):
    return NumberObject(self.val==0)
  def Positive(self):
    return NumberObject(self.val)
  def Unpack(self):
    return NumberObject(self.val)
  def Complement(self):
    raise TypeError
  def RealPart(self):
    return NumberObject(re(self.val))
  def ImaginaryPart(self):
    return NumberObject(im(self.val))
  def Length(self):
    raise TypeError
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
    if arg.Type()!="Number":
      raise TypeError
    return NumberObject(self.val+arg.val)
  def Minus(self,arg):
    if arg.val==0:
      return self.Positive()
    if self.val==arg.val:
      return NumberObject(0)
    if arg.Type()!="Number":
      raise TypeError
    if self.val==0:
      return arg.Negative()
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
    if arg.Type()!="Number":
      raise TypeError
    if arg.val==-1:
      return self.Negative()
    if self.val==-1:
      return arg.Negative()
    return NumberObject(self.val*arg.val)
  def Divide(self,arg):
    if arg.val==0:
      raise DivideByZeroError
    if arg.val==1:
      return self.Positive()
    if arg.val==-1:
      return self.Negative()
    if self.val==arg.val:
      return NumberObject(1)
    if self.val==0:
      return NumberObject(0)
    if arg.Type()!="Number":
      raise TypeError
    if self.val==arg.Negative().val:
      return NumberObject(-1)
    return NumberObject(self.val/arg.val)
  def Modulo(self,arg):
    if arg.Type()!="Number":
      raise TypeError
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
    if arg.Type()!="Number":
      raise TypeError
    return NumberObject(self.val**arg.val)
  def HasMember(self,arg):
    raise TypeError
  def IsMemberOf(self,arg):
    if arg
    return arg.HasMember(self)
  def And(self,arg):
    if self.val==0 or arg.val==0:
      return NumberObject(0)
    return NumberObject(1)
  def Or(self,arg):
    if self.val==0 and arg.val==0:
      return NumberObject(0)
    return NumberObject(1)
  def Intersection(self,arg):
    raise TypeError
  def Union(self,arg):
    raise TypeError
  def SetDifference(self,arg):
    raise TypeError
  def Less(self,arg):
    if im(self.val)!=0 or im(arg.val)!=0:
      raise TypeError
    return NumberObject(self.val<arg.val)
  def LessEqual(self,arg):
    if im(self.val)!=0 or im(arg.val)!=0:
      raise TypeError("Complex Inequalities are not supported")
    return NumberObject(self.val<=arg.val)
  def Greater(self,arg):
    if im(self.val)!=0 or im(arg.val)!=0:
      raise TypeError("Complex Inequalities are not supported")
    return NumberObject(self.val>arg.val)
  def GreaterEqual(self,arg):
    if im(self.val)!=0 or im(arg.val)!=0:
      raise TypeError("Complex Inequalities are not supported")
    return NumberObject(self.val>=arg.val)
  def Equal(self,arg):
    return NumberObject(self.val==arg.val)
  def NotEqual(self,arg):
    return NumberObject(self.val!=arg.val)
  def Subset(self,arg):
    raise TypeError("Type 'Number' does not have Members")
  def SubsetEqual(self,arg):
    raise TypeError("Type 'Number' does not have Members")
  def Superset(self,arg):
    raise TypeError("Type 'Number' does not have Members")
  def SupersetEqual(self,arg):
    raise TypeError("Type 'Number' does not have Members")
  def SetEqual(self,arg):
    raise TypeError("Type 'Number' does not have Members")
  def SetNotEqual(self,arg):
    raise TypeError("Type 'Number' does not have Members")
  def IfThenElse(self,first,last):
    if self.val==0:
      return last.Positive()
    return first.Positive()
    
