b = [2,1,5,3,4]
c = sorted(b)
bribe = 0
for i in range(5):
    print(b.index(c[i]) - i)
    if b.index(c[i]) - i == 2 or b.index(c[i]) - i == -2:
        bribe = bribe + 2
    else:
        bribe = bribe + 1
print(bribe)
