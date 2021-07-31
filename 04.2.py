l=eval(input())
def rgb(l):
    if len(l)==1:
        return l[0]
    else:
        a=0
        b=1
        if l[a]==l[b]:
            a+=1
            b+=1
        if (l[a]=='R' and l[b]=='G') or (l[a]=='G' and l[b]=='R'):
            l[a]='B'
            del l[b]
            return rgb(l)
        elif (l[a]=='R' and l[b]=='B')  or (l[a]=='B' and l[b]=='R'):
            l[a]='G'
            del l[b]
            return rgb(l)
        elif (l[a]=='B' and l[b]=='G') or (l[a]=='G' and l[b]=='B'):
            l[a]='R'
            del l[b]
            return rgb(l)

a=rgb(l)
print(f'"{a}"')