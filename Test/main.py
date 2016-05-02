def lex(arg):
  return list(arg)
def is_NonZero(arg): #If a sequence is NonZero
  return arg in [['1'],['2'],['3'],['4'],['5'],['6'],['7'],['8'],['9']]
def is_Digit(arg): #If a sequence is Digit
  return is_NonZero(arg) or arg==['0']
def is_Number(arg):
  from functools import reduce
  if arg == []:
  	return False
  return (arg == ['0']) or (is_NonZero([arg[0]]) and reduce(lambda x,y:x and y,map(lambda x : is_Digit([x]),arg[0:])))
def is_Atom(arg):
  if arg==[]:
  	return False
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
def is_Mul(arg):
  if is_Unary(arg):
    return True
  else:
    for i in range(len(arg)):
      u=arg[0:i]
      if u != []:
      	t=arg[i:]
      	if t != []:
      		v=t[1:]
      		if v != []:
      			w=t[0]
      			if w != '':
      				if is_Mul(u) and is_MulS([w]) and is_Unary(v):
    			  		return True
    return False
def is_AddS(arg):
  return arg==['+'] or arg==['-']
def is_Add(arg):
  if is_Mul(arg):
    return True
  else:
    for i in range(len(arg)):
      u=arg[0:i]
      if u!=[]:
      	t=arg[i:]
      	if t !=[]:
      		v=t[1:]
      		if v != []:
      			w=t[0]
      			if w != []:
      				if is_Add(u) and is_AddS([w]) and is_Mul(v):
    		  			return True
    return False
