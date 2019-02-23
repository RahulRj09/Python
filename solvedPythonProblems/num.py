# num = input()
# num1 = input()
# count = 0
# if len(num1) == len(num):
#     for i in num:
#         if i in num1:
#             count = count + 1
# print(count)
# if (len(num) and len(num1)) == count:
#     print('Possible')
#
# else:
#     print('Not Possible')

# from collections import Counter as C
# s = input()
# count = C(s)
# print(count)
# print(type(count))
# for x,y in count.items():
#     print(x,y)
# print(count["a"])

# fac=input()
# fac=list(fac)
# for i in range(len(fac)):
# 	j=(int(fac[i]))
# 	j=j*i
#     print(j)
# def fun(n):
#     product = 1
#     for i in range(n,0,-1):
#         product = product * i
#     print(product)
# a = input()
# a = list(a)
# for i in a:
#     n = int(i)
#     fun(n)
# num = int(input())
# list1 = [1,26,3,33,4,52]
# list2 = []
# while True:
#     max = list1[0]
#     for i in range(len(list1)):
#         if max < list1[i]:
#             max = list1[i]
#
#     list2.append(max)
#     list1.remove(max)
#     if len(list2) == num:
#         break
# print(list2)
line = "Hey, how are you"
print(line.split())
print(line.split(' '))
print(line.split(','))
