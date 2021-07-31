a={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'tweleve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'ninteen',20:'twenty',30:'thirty',40:'fourty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred'}
def two(c):
    if c==100:
        return 'hundred'
    elif c>20:
        m=a[c-c%10]
        k=a[c%10]
        return m+" "+k
    else:
        return a[c]

b=int(input())
if b==0:
    print("zero")
if (b//1000000000!=0):
    print(a[b//1000000000]+"arab",end=" ")
    b=b-(b//1000000000)*1000000000
if(b//10000000!=0):
    print(two(b//10000000),"crore",end=" ")
    b=b-(b//10000000)*10000000
if(b//100000!=0):
    print(two(b//100000),"lakh",end=" ")
    b=b-(b//100000)*100000
if(b//1000!=0):
    print(two(b//1000),"thousand",end=" ")
    b=b-(b//1000)*1000
if(b//100!=0):
    print(two(b//100),"hundred",end=" ")
    b=b-(b//100)*100
if b!=0:
    print(two(b))