def check(arr):
    maxcount=1
    count=1
    maxval=arr[0]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                count=count+1
        if maxcount<count:
            maxval=arr[i]
            maxcount=count
        
    return maxval

arr=[1, 3, 2, 1, 4, 1,1]    
print(check(arr))


def frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    print("{} occurs {} times in the list".format(num,counter))
