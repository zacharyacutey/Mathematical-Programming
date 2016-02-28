from sympy import *
class NumberObject:
  def __init__(self,val):
    self.val=Number(val)
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
    
