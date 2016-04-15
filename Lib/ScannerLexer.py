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
  '$ceb': u'\u2308',
  '$def': u'\u225d'
}


def ascii_to_unicode(s):
  i=0
  r=""
  while i<len(s):
    if s[i]==u"\xd7":
      r+="*"
      i+=1
    elif s[i]==u"\xf7":
      r+="/"
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
def next_lex(s,p):
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
def lex(s):
  i=0
  r=[]
  while i<len(s):
    u=next_lex(s,i)
    r.append(u)
    i+=len(u)
  return r
def token_name(l):
  if numeric(l[0]):
    return 'T_NUMBER'
  elif alphabetic(l[0]):
    return 'T_VARIABLE'
  elif l=='+':
    return 'T_ADD'
  elif l=='-':
    return 'T_MINUS'
  elif l=='*':
    return 'T_MULTIPLY'
  elif l=='/':
    return 'T_DIVIDE'
  elif l=='%':
    return 'T_MOD'
  elif l=='^':
    return 'T_POWER'
  elif l=='~':
    return 'T_NOT'
  elif l=='<':
    return 'T_LESS'
  elif l=='>':
    return 'T_GREATER'
  elif l==':':
    return 'T_COLON'
  elif l=='{':
    return 'T_LEFTBRACE'
  elif l=='}':
    return 'T_RIGHTBRACE'
  elif l==',':
    return 'T_COMMA'
  elif l=='=':
    return 'T_EQUAL'
  elif l==';':
    return 'T_SEMICOLON'
  elif l=='\\':
    return 'T_SETMINUS'
  elif l=='(':
    return 'T_LEFTPAREN'
  elif l==')':
    return 'T_RIGHTPAREN'
  elif l=='[':
    return 'T_LEFTBRACKET'
  elif l==']':
    return 'T_RIGHTBRACKET'
  elif l==ascii_to_unicode('$uni'):
    return 'T_UNION'
  elif l==ascii_to_unicode('$img'):
    return 'T_IMAGINARY'
  elif l==ascii_to_unicode('$pos'):
    return 'T_POSITIVE'
  elif l==ascii_to_unicode('$neg'):
    return 'T_NEGATIVE'
  elif l==ascii_to_unicode('$equ'):
    return 'T_ISEQUAL'
  elif l==ascii_to_unicode('$els'):
    return 'T_ELSE'
  elif l==ascii_to_unicode('$ior'):
    return 'T_OR'
  elif l==ascii_to_unicode('$rea'):
    return 'T_REAL'
  elif l==ascii_to_unicode('$pro'):
    return 'T_PRODUCT'
  elif l==ascii_to_unicode('$leq'):
    return 'T_LESSEQUAL'
  elif l==ascii_to_unicode('$unp'):
    return 'T_UNPACK'
  elif l==ascii_to_unicode('$neq'):
    return 'T_NOTEQUAL'
  elif l==ascii_to_unicode('$seq'):
    return 'T_SETEQUAL'
  elif l==ascii_to_unicode('$len'):
    return 'T_LENGTH'
  elif l==ascii_to_unicode('$mem'):
    return 'T_MEMBER'
  elif l==ascii_to_unicode('$flb'):
    return 'T_BEGINFLOOR'
  elif l==ascii_to_unicode('$fle'):
    return 'T_ENDFLOOR'
  elif l==ascii_to_unicode('$and'):
    return 'T_AND'
  elif l==ascii_to_unicode('$ift'):
    return 'T_IF'
  elif l==ascii_to_unicode('$sup'):
    return 'T_SUPERSET'
  elif l==ascii_to_unicode('$sum'):
    return 'T_SUM'
  elif l==ascii_to_unicode('$int'):
    return 'T_INTERSECT'
  elif l==ascii_to_unicode('$cee'):
    return 'T_CEILINGEND'
  elif l==ascii_to_unicode('$sbe'):
    return 'T_SUBSETEQUAL'
  elif l==ascii_to_unicode('$spe'):
    return 'T_SUBSET'
  elif l==ascii_to_unicode('$fun'):
    return 'T_FUNCTION'
  elif l==ascii_to_unicode('$com'):
    return 'T_COMPLEMENT'
  elif l==ascii_to_unicode('$sne'):
    return 'T_SETNOTEQUAL'
  elif l==ascii_to_unicode('$geq'):
    return 'T_GREATEREQUAL'
  elif l==ascii_to_unicode('$ceb'):
    return 'T_CEILINGBEGIN'
def tokenize(s):
  return [(i,token_name(i)) for i in lex(coding(s))]
