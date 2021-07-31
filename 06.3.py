b = ""
while True:
    a = input()
    b = b + a
    if a == "}":
        break
b = b.replace(" ", "")
a = eval(b)
list1 = list(i[1] for i in a.items())
count = 0
while len(list1) != 0:
    c = 0
    l1 = []

    for i in list1:
        m = 0
        comp = []
        for j in list1:
            if i != j:
                if len(set(i).intersection(set(j))) != 0:
                    m = m + 1
                    comp = list(set(i).intersection(set(j)))
        if c < m:
            c = m
            l1 = comp
    list2 = []
    if (len(l1) == 0):
        count = count + len(list1)
        break
    else:

        for k in list1:

            if l1[0] not in k:
                list2.append(k)
        list1 = list2

    count = count + 1

print(count)