def unique(arr):
   
    seen=set()
    for i in arr:
        if i in seen:
            return False
        else:
            seen.add(i)
    return True        
print(unique("abcee"))   


def unique(s):
    a=set(s)
    if(len(a)==len(s)):
        return True
    return False    
print(unique("abcee"))      
