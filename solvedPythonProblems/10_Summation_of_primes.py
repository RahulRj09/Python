# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
i = 2
prime_list= []
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
prime_sum = 0
while i<2000000:
    ulist = []
    ulist.append(i)
    result = get_prime(ulist)
    if result == False:
        i = i + 1
    else:
        prime_sum = prime_sum + i
        i = i + 1
print(prime_sum)

#142913828922
