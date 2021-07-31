a = int(input())
c = int(input())
b = a
for i in range(a):
    for k in range(b - i - 1):
        print(' ', end='')
    print('*', end='')
    for m in range(2 * (i - 1) + 1):
        if i != c - 1:
            print(" ", end='')
        else:
            print("*", end='')

    if (i > 0):
        print('*')
    else:
        print()s