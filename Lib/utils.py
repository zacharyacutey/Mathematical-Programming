#TODO, add unicode escapes!
atd={
  "$img":"ℑ",
  "$rea":"ℜ",
  "$ift":"→",
  "$fun":"↦",
  "$els":"↛",
  "$com":"∁",
  "$mem":"∈",
  "$unp":"∋",
  "$pro":"Π",
  "$sum":"Σ"
  "$pos":"∔",
  "$and":"∧",
  "$ior":"∨",
  "$int":"∩",
  "$uni":"∪",
  "$neg":"∸",
  "$equ":"≟",
  "$neq":"≠",
  "$seq":"≡",
  "$sne":"≢",
  "$leq":"≤",
  "$geq":"≥",
  "$sub":"⊂",
  "$sup":"⊃",
  "$sbe":"⊆",
  "$spe":"⊇",
  "$ceb":"⌈",
  "$cee":"⌉",
  "$flb":"⌊",
  "$fle":"⌋",
  "$len":"ω"
}
#Just some random utilities that don't fit in to the (soon to be) massive compiler/tokenizer/transpiler/interpreter/parser page
#To Do:
#ALLOW WINDOWS FUNCTIONALITY!!!!!!!!!!!!!!!!
def ascii_to_unicode(s):
  i=0
  r=""
  while i<len(s):
    if s[i]=="*":
      r+="×"
      i+=1
    elif s[i]=="/":
      r+="÷"
      i+=1
    elif s[i:i+5] in atd.keys():
      r+=atd[s[i:i+5]]
      i+=5
    else:
      r+=s[i]
      i+=1
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
    return "∔"
  if c=="-":
    return "∸"
  return c
def replace_unary(s):
  r=[]
  for i in range(len(s)):
    if is_unary(s,i):
      r.append(unary_char(s[i]))
    else:
      r.append(c)
  return ''.join(r)
def coding(s):return replace_unary(remove_w(ascii_to_unicode(s)))
