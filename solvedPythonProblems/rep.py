s = str(input())
n = int(input())
d = ""
for i in range(n):
    d = d + s
flag = 0
for i in d[:n]:
    if i == 'a':
        flag = flag + 1
print(flag)
