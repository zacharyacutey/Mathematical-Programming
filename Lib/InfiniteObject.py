from __future__ import division
from NumberObject import Number
from sympy import re,im,Abs,floor,ceiling
from sympy import S as _Number
import sympy
import copy
import inspect
MIN_N=-100
MAX_N=100
MIN_D=100
MAX_D=100
SET_OF_ALL=set()
for i in range(MIN_N,MAX_N+1):
  for j in range(MIN_D,MAX_D+1):
    if not j==0:
      SET_OF_ALL.add(Number(_Number(i)/j))
NEW_SET=set()
for i in SET_OF_ALL:
  for j in SET_OF_ALL:
    NEW_SET.add(i.Add(j.Multiply(Number(sympy.sqrt(-1)))))
SET_OF_ALL=NEW_SET
def DoSomethingHelper(arg): #Am in no way sure how to describe this
  t=set()
  for i in arg:
    for j in SET_OF_ALL:
      t.add(i.Add(j))
  return t
def DoSomething(arg):
  t=set()
  for i in SET_OF_ALL:
    t.add(i)
  i=1
  while True:
    if i==arg:
      return t
    t=DoSomeThingHelper(t)
    i+=1
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
    val=DoSomething(len(inspect.getargspec(self.val)[0])+len(inspect.getargspec(self.val)[1] if inspect.getargspec(self.val)[1]!=None else []))
    for i in val:
      if type(i)!=tuple and type(i)!=list:
        if self.val(i)[1].val!=0:
          return Number(1)
    return Number(0)
  def IsMemberOf(self,arg):
    return arg.HasMember(self)
  def And(self,arg):
    raise TypeError
  def Or(self,arg):
    raise TypeError
  def Union(self,arg):
    return Infinite(lambda n : (n,n.IsMemberOf(self).Or(n.IsMemberOf(arg))))
  def Intersection(self,arg):
    return Infinite(lambda n : (n,n.IsMemberOf(self).And(n.IsMemberOf(arg))))
  def SetDifference(self,arg):
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
    return self.SetEqual(arg)
  def NotEqual(self,arg):
    return self.SetNotEqual(arg)
  def Subset(self,arg):
    return self.SubsetEqual(arg).And(self.SetNotEqual(arg))
  def SubsetEqual(self,arg):
    val=DoSomething(len(inspect.argspec(self.val)[0])+len(inspect.argspec(self.val)[1] if inspect.argspec(self.val)[1]!=None else []))
    for i in val:
      if type(i)!=tuple and type(i)!=list:
        if self.val(i)[1].Equal(Number(0)):
          return Number(0)
      if self.val(*i)[1].Equal(Number(0)):
        return Number(0)
    return Number(1)
      
  def Superset(self,arg):
    return self.SubsetEqual(arg).Not()
  def SupersetEqual(self,arg):
    return self.Subset(arg).Not()
  def SetEqual(self,arg):
    return self.SupersetEqual(arg).And(self.SubsetEqual(arg))
  def SetNotEqual(self,arg):
    return self.SetEqual(arg).Not()
  def IfThenElse(self,arg):
    raise TypeError
  def Call(self,*args):
    raise TypeError
  def InfiniteSum(self):
    raise TypeError
  def InfiniteProduct(self):
    raise TypeError
