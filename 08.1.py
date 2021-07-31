import itertools
a=int(input())
l=[]
lst=list(map(str,itertools.product(([0,1]),repeat=a)))
c=0
for i in lst:
    if "1, 1" in i:
        c=c+1
print(2**a-c-1)