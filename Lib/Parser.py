from ScannerLexer import *
def seperate_lines(s_):
  s=s_.split(";")
  r=[]
  for i in s:
    if i!="":
      r.append(i)
  return r
def is_lambda_expression(arg):
  """
  Tells if a string is a lambda expresion, EBNF 'Function'
  """
  count = 0
  for i in [j[0] for j in arg]: #Make sure for the stream of tokens
    if count == 0:
      if i == atd['$fun']:
        return True
    elif count < 0:
      print("DAFUQ? AN ERROR DID APPEAR! I SHOULD BE THE ONLY ONE USING THIS, SO STOP MAKING TYPOS B****!")
      exit()
    else:
      if i == '(':
        count += 1
      if i == ')':
        count -= 1
  return False
