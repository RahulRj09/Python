# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
i = 2
prime_list= []
# def check_prime(number):
#     if number%2 == 0  or number%3 == 0 or number%5 == 0 or number%7 == 0:
#         return False
#     else:
#         return True
def get_prime(ulist):#function that takes a list and returns a list of prime numbers only
 plist = []#list that will contain prime numbers
 for i in ulist:
     tlist = []
     num = int(i**0.5)
     for x in range(1,num+1):
         if i == 1:
             continue
         elif i%x == 0:
             tlist.append(x)
     if len(tlist) == 1:
         plist.append(i)
     if len(plist) == 1:
         return True
     else:
         return False
while True:
    ulist = []
    if len(prime_list) == 10001:
        break
    ulist.append(i)
    result = get_prime(ulist)
    if result == False:
        i = i + 1
    else:
        prime_list.append(i)
        i = i + 1
print(prime_list[-1])



#answer
#104743
