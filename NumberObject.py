from sympy import *
class NumberObject:
  def __init__(self,val):
    self.val=Number(val)
  def Neg(self):
    return NumberObject(-self.val)
