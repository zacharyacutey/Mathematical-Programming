"""
TODO: Implement nested Finite's
"""
from NumberObject import Number
from InfiniteObject import Infinite
from __future__ import division
from sympy import ceiling,floor,re,im,Abs
sortNumber=lambda n : [Number(j) for j in sorted([i.val for i in n])]
class Finite:
  def __init__(self,*args):
    for i in args:
      if i.Type=="Infinite" or i.Type=="Function":
        raise TypeError
      if i.Type=="Finite":
        raise NotImplementedError
    self.val=args
    i=0
    while i<len(self.val):
      j=i+1
      while j<len(self.val):
        if self.val[i].val==self.val[j].val:
          self.val.pop(i)
          i-=1
        j+=1
      i+=1
    self.val=sortNumber(self.val)
    """
    TODO Fix the sorting for a finite set if the set has a finite set
    """
    
  @property
  def Type(self):
    return "Finite"
  def Negative(self):
    raise TypeError
  def Not(self):
    raise TypeError
  def Positive(self):
    return Finite(*[i.val for i in self.val])
  def Unpack(self):
    if len(self.val)==1:
      return self.val[0].Positive()
    return self.Positive()
  def Complement(self):
    return Infinite(lambda n : (n,(n.IsMemberOf(self).Not())))
  def RealPart(self):
    raise TypeError
  def ImaginaryPart(self):
    raise TypeError
  def Length(self):
    return Number(len(self.val))
  def Floor(self):
    raise TypeError
  def Ceiling(self):
    raise TypeError
  def AbsoluteValue(self):
    raise TypeError
  def Add(self,arg):
    return self.Union(arg)
  def Minus(self,arg):
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
  def Modulo(self,arg):
    raise TypeError
  def Power(self,arg):
    if arg.val==0:
      return Number(1)
    if arg.val==1:
      return self.Positive()
    raise TypeError
  def HasMember(self,arg):
    for i in self.val:
      if i.val==arg.val:
        return Number(1)
    return Number(0)
  def IsMemberOf(self,arg):
    raise NotImplementedError
  def And(self,arg):
    raise TypeError
  def Or(self,arg):
    raise TypeError
  def Union(self,arg):
    if arg.Type=="Finite":
      return Finite(*(self.val+arg.val))
    return Infinite(lambda n : (n,n.IsMemberOf(self).Or(n.IsMemberOf(arg))))
  def Intersection(self,arg):
    if arg.Type=="Finite": #Must implement this later!
      pass
    return Infinite(lambda n : (n,n.IsMemberOf(self).And(n.IsMemberOf(arg))))
  def SetDifference(self,arg):
    if arg.Type=="Finite":
      pass
    return Infinite(lambda n : (n,n.IsMemberOf(self).And(n.IsMemberOf(arg).Not()))
  def Less(self,arg):
    raise TypeError
  def LessEqual(self,arg):
    raise TypeError
  def Greater(self,arg):
    raise TypeError
  def GreaterEqual(self,arg):
    raise TypeError
  def Equal(self,arg):
    return Number(self.val==arg.val)
  def NotEqual(self,arg):
    return Number(self.val!=arg.val)
  def Subset(self,arg):
    for i in self.val:
      if bool(i.IsMemberOf(arg).Not().val):
        return Number(0)
    if self.Length()==arg.Length():
      return Number(0)
    return Number(1)
  def Superset(self,arg):
    return arg.Subset(self)
  def SubsetEqual(self,arg):
    for i in self.val:
      if bool(i.IsMemberOf(arg).Not().val):
        return Number(0)
    return Number(1)
  def SupersetEqual(self,arg):
    return arg.SubsetEqual(self)
  def SetEqual(self,arg):
    if arg.Type!="Finite" and arg.Type!="Infinite":
      raise TypeError
    return self.Equal(arg)
  def SetNotEqual(self,arg):
    return self.Equal(arg).Not()
  def IfThenElse(self,first,last):
    raise TypeError
