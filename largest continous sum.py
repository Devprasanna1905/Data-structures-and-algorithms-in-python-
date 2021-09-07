def large(arr):
    if(len(arr)==0):
        return 0
    else:    
        currentsum=maxsum=arr[0]
        for i in arr[1:]:
            currentsum=max(currentsum+i,i)
            maxsum=max(currentsum,maxsum)
    return maxsum  
print(large([1,2,-3,4,-5,-5,]))
            
