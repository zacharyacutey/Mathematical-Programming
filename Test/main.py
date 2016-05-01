def lex(arg):
  return list(arg)
def is_NonZero(arg): #If a sequence is NonZero
  return arg in [['1'],['2'],['3'],['4'],['5'],['6'],['7'],['8'],['9']]
def is_Digit(arg): #If a sequence is Digit
  return is_NonZero(arg) or arg==['0']
def is_Number(arg):
  from functools import reduce
  return (arg == ['0']) or (is_NonZero([arg[0]]) and reduce(lambda x,y:x and y,map(lambda x : is_Digit([x]),arg[0:])))
def is_Atom(arg):
  if is_Number(arg):
    return True
  else:
    u = arg[1:len(arg)-1]
    return arg[0] == '(' and is_Add(u) and arg[-1]==')'
def is_UnaryS(arg):
  return arg==['_']
def is_Unary(arg):
  if is_Atom(arg):
    return True
  else:
    return is_UnaryS([arg[0]]) and is_Atom(arg[1:])
def is_MulS(arg):
  return arg==['*'] or arg==['/']
