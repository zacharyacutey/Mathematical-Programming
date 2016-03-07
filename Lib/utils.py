atd={"$img":"ℑ"}
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
