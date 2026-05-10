def selectionsort(arr):
    for i in range(len(arr)):
	    idx = i
	    for j in range(i+1, len(arr)):
		    if A[idx] > arr[j]:
			    idx = j
	    #swapping min element with first element		
	    arr[i], arr[idx] = arr[idx], arr[i]
    return arr
    
print ("Sorted array: ")
A=[23,45,1,5,65,100]
print(selectionsort(A))
