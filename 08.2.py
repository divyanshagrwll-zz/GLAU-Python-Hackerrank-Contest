a=eval(input())
b=eval(input())
for i in range(len(a)):
    lt=[]
    for k in a[i]:
        lt.append(k)
    lt.sort()
    c=''
    for k in lt:
        c=c+k
    a[i]=c
for i in range(len(b)):
    lt=[]
    for k in b[i]:
        lt.append(k)
    lt.sort()
    c=''
    for k in lt:
        c=c+k
    b[i]=c
print(len(set(a).intersection(set(b))))