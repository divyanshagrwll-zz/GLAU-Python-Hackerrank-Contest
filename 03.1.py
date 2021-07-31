a=list(input().split(" "))
c=0
m=0
for i in a:
    for k in range(1+c,len(a)):
       t=int(i)&int(a[k])
       if t>m :
           m=t
    c=c+1
print(m)