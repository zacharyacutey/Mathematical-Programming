def is_NonZero(arg): #If a sequence is NonZero
  return arg in [['1'],['2'],['3'],['4'],['5'],['6'],['7'],['8'],['9']]
def is_Digit(arg): #If a sequence is Digit
  return is_NonZero(arg) or arg==['0']
def is_Number(arg):
  from functools import reduce
  return (arg == ['0']) or (is_NonZero(arg[0]) and reduce(lambda x,y:x and y,map(lambda x : is_Digit(x),arg)))
