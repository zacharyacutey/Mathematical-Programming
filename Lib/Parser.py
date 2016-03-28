from ScannerLexer import *
def seperate_lines(s_):
  s=s_.split(";")
  r=[]
  for i in s:
    if i!="":
      r.append(i)
  return r
