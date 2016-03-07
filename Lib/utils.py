atd={"$img":"ℑ"}
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
def next_sep(s_,p):
  s=s_[p:]
  #Resume here
