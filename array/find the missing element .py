def find(arr1,arr2):
    arr1.sort()
    arr2.sort()
    for i in range(len(arr1)):
        if arr1[i]!=arr2[i]:
            return arr1[i]
print(find([1,2,3,4,5,6,7],[3,7,2,1,4,6]))
