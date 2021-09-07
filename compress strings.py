def compress(s):
    r=""
    l=len(s)
    if(l==0):
        return "enter a valid string"
    if(l==1):
        return s+"1"
    i=1
    count=1
    last=s[0]    
    while(i<l):
        
        if(s[i]==s[i-1]):
            count=count+1
        else:
            r=r+s[i-1]+str(count)
            count=1
        i=i+1
    r=r+s[i-1]+str(count)
    return r
print(compress("AAAAAAAABBBBBBB"))    
