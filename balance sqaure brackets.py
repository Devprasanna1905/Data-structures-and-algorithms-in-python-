def balance(s):
    l=[]
    for i in s:
        if i=="[":
            l.append(i)
        elif i=="]":
            if l.pop() !="[":
                return False
    return len(l)==0
print(balance("[[]"))    
