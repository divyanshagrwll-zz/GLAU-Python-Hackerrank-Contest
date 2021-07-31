n=int(input())
l=list(map(int,input().split()))
o=int(input())
for i in range(0,o):
    q=int(input())
    count=0
    for j in l:
        if q>j:
            count += 1
    print(count)