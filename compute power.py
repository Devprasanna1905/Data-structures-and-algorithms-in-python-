def compute(n,p):
    result=1
    for i in range(1,p+1):
        result=n*result
    return result

print(compute(2,3))
