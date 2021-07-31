1
def findMaxLen(string):
2
    n = len(string)
3
    stk = []
4
    stk.append(-1)
5
    result = 0
6
    for i in range(n):
7
        if string[i] == '(':
8
            stk.append(i)
9
        else:  
10
            if len(stk) != 0:
11
               stk.pop()
12
            if len(stk) != 0:
13
                result = max(result,
14
                             i - stk[len(stk)-1])
15
            else:
16
                stk.append(i)
17
    return result
18
​
19
string =input()
20
print(findMaxLen(string))