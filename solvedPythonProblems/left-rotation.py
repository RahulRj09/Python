a = input()
b = input()
b = b.split()
a = a.split()
l = []
t = int(a[-1])
s = int(a[0])
for i in b:
    l.append(int(i))
m = []
for i in range(s):
    m.append(0)
for i in range(s):
    m[i-t] = l[i]
for i in m:
    print(i, end=' ')


# for x in  range(t):
#     for i in l[1:]:
#         m.append(i)
#     else:
#         m.append(l[0])
#     l.clear()
#     l = m[:]
#     m.clear()
# for i in l:
#      print(str(i), end=' ')
