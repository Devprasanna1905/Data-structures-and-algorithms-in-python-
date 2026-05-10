def rec_sum(n):
    if len(str(n)) == 1:
        return n
    else:
        return n%10+rec_sum(n//10)
print(rec_sum(114))

#using map and sum fucntions
n=114
a=list(map(int,str(n)))
print(sum(a))
