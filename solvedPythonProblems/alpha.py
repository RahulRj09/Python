test = int(input())
add = []
list1 = []
list2 = []
bribe = 0
too_chaotic = []
for d in range(test):
    list1.append(int(input()))
    list2.append(input())
    for b in list2:
        b = b.split()
        for x in range(len(b)):
            b[x] = int(b[x])
        c = sorted(b)
    for i in range(len(c)):
            if b[i] >= c[i]:
                omega = c.index(b[i]) - i
                if (omega > 2) or (omega < -2) or len(b) == 1:
                    add.append('Too chaotic')
                    too_chaotic.append(b)
    if b not in too_chaotic:
        while True:
            for i in range(len(b)-1):
                if b[i] > b[i+1]:
                    b[i+1],b[i] = b[i],b[i+1]
                    bribe = bribe + 1
            if b == c:
                break
        if bribe!=0:
            add.append(bribe)
            bribe = 0



for i in range(test):
    if add[i] == 'Too chaotic':
        print("Too chaotic")
    else:
        print(int(add[i]))
