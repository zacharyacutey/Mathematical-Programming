def is_NonZero(arg):
  return arg in [['1'],['2'],['3'],['4'],['5'],['6'],['7'],['8'],['9']]
def is_Digit(arg):
  return is_NonZero(arg) or arg==['0']
def is_Number(arg):
  from functools import reduce
  return is_NonZero(arg) and reduce(lambda x,y:x and y,map(lambda x : is_Digit(x),arg))
