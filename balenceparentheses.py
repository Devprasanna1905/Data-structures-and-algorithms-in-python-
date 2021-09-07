def check(s):
    if(len(s)%2!=0):
        return False
    opening=set("({[")    
    matches=( [("(",")"),("{","}"),("[","]")] )
    stack=[]
    for i in s:
        if i in opening:
            stack.append(i)
        else:
            if(len(stack)==0):
                return False
            last=stack.pop()  
            if(last,i) not in matches:
                return False
    return len(stack)==0        
