def check(p,l,out=None):
    if out is None:
        out=[]
        
    for i in l:
        if p.startswith(i):
            out.append(i)
            return check(p[len(i):],l,out)
    return out        

p="themanran"
l=["the","man","ran"]
out=[]
print(check(p,l,out))
            
