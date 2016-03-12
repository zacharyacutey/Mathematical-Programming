atd={
  '$uni': u'\u222a',
  '$img': u'\u2111',
  '$pos': u'\u2214',
  '$neg': u'\u2238',
  '$equ': u'\u225f',
  '$els': u'\u219b',
  '$ior': u'\u2228',
  '$rea': u'\u211c',
  '$pro': u'\u03a0',
  '$leq': u'\u2264',
  '$unp': u'\u220b',
  '$neq': u'\u2260',
  '$seq': u'\u2261',
  '$len': u'\u03c9',
  '$mem': u'\u2208',
  '$flb': u'\u230a',
  '$fle': u'\u230b',
  '$and': u'\u2227',
  '$ift': u'\u2192',
  '$sup': u'\u2283',
  '$sum': u'\u03a3',
  '$int': u'\u2229',
  '$cee': u'\u2309',
  '$sbe': u'\u2286',
  '$sub': u'\u2282',
  '$spe': u'\u2287',
  '$fun': u'\u21a6',
  '$com': u'\u2201',
  '$sne': u'\u2262',
  '$geq': u'\u2265',
  '$ceb': u'\u2308'
}

S_NUMBER=0
S_SYMBOL=1
S_VARIABLE=2

def ascii_to_unicode(s):
  i=0
  r=""
  while i<len(s):
    if s[i]=="*":
      r+=u"\xd7"
      i+=1
    elif s[i]=="/":
      r+=u"\xf7"
      i+=1
    elif s[i:i+4] in atd.keys():
      r+=atd[s[i:i+4]]
      i+=4
    else:
      r+=s[i]
      i+=1
  else:
    return s
  return r
def remove_w(s):
  i=0
  r=""
  while i<len(s):
    if s[i]=="\n" or s[i]=="\r" or s[i]=="\t" or s[i]==" ":
      i+=1
    else:
      r+=s[i]
      i+=1
  else: #Love this!
   return s
    
  return r
def alphabetic(c):
  return c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def numeric(c):
  return c in "0123456789"
def alphanumeric(c):
  return alphabetic(c) or numeric(c)
def is_unary(s,p):
  if p==0:
    return True
  return not alphanumeric(s[p-1])
def unary_char(c):
  if c=="+":
    return ascii_to_unicode("$pos")
  if c=="-":
    return ascii_to_unicode("$neg")
  return c
def replace_unary(s):
  r=[]
  for i in range(len(s)):
    if is_unary(s,i):
      r.append(unary_char(s[i]))
    else:
      r.append(s[i])
  return ''.join(r)
def coding(s):return replace_unary(remove_w(ascii_to_unicode(s)))
def next_sep(s,p):
  r=""
  if alphabetic(s[p]):
    i=p
    while i<len(s):
      if alphanumeric(s[i]):
        r+=s[i]
      else:
        return r
      i+=1
  elif numeric(s[p]):
    i=p
    while i<len(s):
      if numeric(s[i]):
        r+=s[i]
      else:
        return r
      i+=1
  else:
    return s[p]
  return r
def sep(s):
  i=0
  r=[]
  while i<len(s):
    u=next_sep(s,i)
    r.append(u)
    i+=len(u)
  return r
