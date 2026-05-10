def resum(n):
    if n == 0:
        return 0
    else:
        return n + resum(n-1)
print(resum(12))      
