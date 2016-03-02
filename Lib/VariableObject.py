from __future__ import division
from sympy import re,im,Abs,floor,ceiling
class Variable:
  def __init__(self,val):
    self.val=val
  @property
  def Type(self):
    return self.val.Type
  def Positive(self):
    return self.val.Positive()
  def Negative(self):
    return self.val.Negative()
  def Complement(self):
    return self.val.Complement()
  def Not(self):
    return self.val.Not()
  def Unpack(self):
    return self.val.Unpack()
