a = int(input())
b = input()
b = b.split()
count = 0
for i in range(a):
    b[i] = int(b[i])
while True:
    for i in range(a-1):
            if b[i] > b[i+1]:
                b[i+1],b[i] = b[i],b[i+1]
                count = count + 1
    if b == sorted(b):
        break
print('Array is sorted in '+ str(count) + ' swaps.')
print('First Element: ' + str(b[0]))
print('Last Element: ' + str(b[-1]))
