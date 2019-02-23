a = int(input())
b = str(input())
c = []
sum = 0
valley = 0
for i in b:
    if i == "U":
        c.append(1)
    else:
        c.append(-1)
for i in range(a):
    if c[i] == -1:
        if sum == 0:
            valley = valley + 1
    sum = sum + c[i]
print(valley)
