n = int(input())
ul = input()
ul = ul.split()
count = 0
for i in range(n):
    ul[i] = int(ul[i])
ol = sorted(ul)
while True:
    for i in range(n-1):
            if ul[i] > u;[i+1]:
                u;[i+1],ul[i] = ul[i],ul[i+1]
                count = count + 1
    if ul == ol:
        break
print(count)
