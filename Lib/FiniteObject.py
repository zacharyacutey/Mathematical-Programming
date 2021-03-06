from __future__ import division
from NumberObject import Number
from InfiniteObject import Infinite
from sympy import ceiling,floor,re,im,Abs
#Do not touch the sortNumber Function, it's my perfectly working masterpiece!
sortNumber=lambda n : [(Number(j) if type(j)!=tuple else Finite(list(j)))for j in sorted([(i.val if type(i.val)!=list else tuple(sortNumber(i.val))) for i in n])]
class Finite:
  def __init__(self,*args):
    for i in args:
      if i.Type=="Infinite" or i.Type=="Function":
        raise TypeError
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
    if arg.val==0: return Number(0)
    return self.Union(arg)
  def Minus(self,arg):
    if arg.val==0: return Number(0)
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
      if bool(i.Equal(arg).val):
        return Number(1)
    return Number(0)
  def IsMemberOf(self,arg):
    return arg.HasMember(self)
  def And(self,arg):
    raise TypeError
  def Or(self,arg):
    raise TypeError
  def Union(self,arg):
    if arg.Type=="Finite":
      return Finite(*(self.val+arg.val))
    return Infinite(lambda n : (n,n.IsMemberOf(self).Or(n.IsMemberOf(arg))))
  def Intersection(self,arg):
    if arg.Type=="Finite":
      t=Finite()
      for i in self.val:
        if i in arg.val:
          t=t.Union(i)
      return t
    return Infinite(lambda n : (n,n.IsMemberOf(self).And(n.IsMemberOf(arg))))
  def SetDifference(self,arg):
    if arg.Type=="Finite":
      t=Finite()
      for i in self.val:
        if not ( i in arg.val ):
          t=t.Union(i)
      return t
    return Infinite(lambda n : (n,n.IsMemberOf(self).And(n.IsMemberOf(arg).Not())))
  def Less(self,arg):
    raise TypeError
  def LessEqual(self,arg):
    raise TypeError
  def Greater(self,arg):
    raise TypeError
  def GreaterEqual(self,arg):
    raise TypeError
  def Equal(self,arg):
    if arg.Type=="Infinite":
      r=True
      for i in self.val:
        if i.IsMemberOf(arg).Not():
          return False
    return Number(self.val==arg.val)
  def NotEqual(self,arg):
    return self.Equal(arg).Not()
  def Subset(self,arg):
    for i in self.val:
      if bool(i.IsMemberOf(arg).Not().val):
        return Number(0)
    if arg.Type=="Infinite":
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
  def Call(self,*args):
    raise TypeError
  def InfiniteSum(self):
    raise TypeError
  def InfiniteProduct(self):
    raise TypeError
  def __str__(self):
    return str({str(i) for i in self.val})
