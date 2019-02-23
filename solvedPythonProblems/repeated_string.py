s = str(input())
n = int(input())
num = 0
a = 0
number = 0
for i in s:
    if 'a' in i:
        number = number + 1
for i in s:
    a = len(s)
    num = int(n/a)
num = num*number
no = n % a
for i in s[:no]:
    if "a" in i:
        num = num + 1
print(num)
