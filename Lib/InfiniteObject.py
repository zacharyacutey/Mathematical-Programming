from NumberObject import Number
from FiniteObject import Finite
from __future__ import division
from sympy import re,im,Abs,floor,ceiling
class Infinite:
  #Infinite paramteter takes local vars and returns a tuple consisting of (value,condition)
  def __init__(self,val):
    self.val=val
  @property
  def Type(self):
    return "Infinite"
  def Negative(self):
    raise TypeError
  def Not(self):
    raise TypeError
