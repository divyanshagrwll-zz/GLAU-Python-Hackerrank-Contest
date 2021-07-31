l=list(input())
a=len(l)
if(a%2!=0):
    print("Odd length.")
else:
    for i in range(0,a,2):
        temp=l[i]
        l[i]=l[i+1]
        l[i+1]=temp
    b="".join(l)
    print(b)