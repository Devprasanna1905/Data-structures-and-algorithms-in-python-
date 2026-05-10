def pairsum(arr,k):
    if(len(arr)<2):
        return "enter more"
    seen=set()
    output=set()
    for i in arr:
        target=k-i
        if target not in seen:
            seen.add(i)
        else:
            output.add( (min(i,target)), max(i,target))
        print("/n".join(map(str,list(output))))  
print(pairsum([1,2,3,4,5],4))        
