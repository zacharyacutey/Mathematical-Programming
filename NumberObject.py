from sympy import *
class NumberObject:
  def __init__(self,val):
    self.val=Number(val)
  def Neg(self):
    return NumberObject(-self.val)
  def Not(self):
    return NumberObject(1 if self.val==0 else 0)
  def Pos(self):
    return NumberObject(self.val)
