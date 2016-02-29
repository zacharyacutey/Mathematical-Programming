from __future__ import division
try:
  print(u"αμπλ")
except UnicodeTranslateError,UnicodeError,UnicodeEncodeError,UnicodeDecodeError:
  raise NotImplementedError("Sorry, I have not implemented your system's unicode")
try:
  from sympy import re,im,Number,Abs,floor,ceiling
except ImportError:
  raise RuntimeError("You must install sympy and any of its dependencies")
