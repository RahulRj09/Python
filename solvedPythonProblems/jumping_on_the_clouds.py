a = int(input())
b = str(input())
b = b.split()
c = []
for i in range(len(b)):
    if b[i] == '0':
        c.append(i)
print(b,c)
steps = 0
i = 0
while True:
    if c[i] == c[-1]:
        break
    elif (c[i] + 2) in c:
        steps = steps + 1
        i = c.index(c[i]+2)
    elif (c[i] + 1) in c:
        steps = steps + 1
        i = c.index(c[i]+1)
    print(steps)
print(steps)
