from utils import *
def sep(s):
  i=0
  r=[]
  while i<len(s):
    u=next_sep(s,i)
    r.append(u)
    i+=len(u)
  return r
