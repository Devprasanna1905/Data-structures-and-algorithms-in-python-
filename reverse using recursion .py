#this solution does not use slicing operator
def check(s):
  if(len(s)<=1):
    return s
  else:
    return check(s[1:])+s[0]
 print(check("hello")) 
  
