def binarysearch(arr,n):
    first=0
    last=len(arr)-1
    while first<=last:
        mid=first+(last-first)//2
        if arr[mid]==n:
            return True
        else:
            if n<arr[mid]:
                last=mid-1
            else:
                first=mid+1
    return False

arr=[1,2,3,4,5,6,7,8]
n=6
print(binary(arr,n))
