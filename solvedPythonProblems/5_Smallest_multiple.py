 # Smallest multiple
 # Problem 5
 # 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
 # What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def get_prime(ulist):#function that takes a list and returns a list of prime numbers only
 plist = []#list that will contain prime numbers
 for i in ulist:
     tlist = []
     for x in range(1,i):
         if i == 1:
             continue
         elif i%x == 0:
             tlist.append(x)
     if len(tlist) == 1:
         plist.append(i)
 return((plist))

ulist = [i for i in range(1,21)]#list of numbers whose multiple we have to determine
prime_list = get_prime(ulist)#calling function get prime
product = 1#multiple will be stored in this variable
for i in prime_list:
 product = product * i#multiplying all the prime numbers
non_prime_list = []#list for all the composite numbers
for i in range(1,21):
 if product%i != 0:
     non_prime_list.append(i)#findind all the non prime numbers which are not a factor of our product
def get_factors(number):
 list_fact = []
 for i in range(1,number+1):
     if number % i ==0:
         list_fact.append(i)
 return list_fact#function that take a number and returns its factors eg. 8 = [2 , 4]
for i in non_prime_list:
 factors = get_factors(i)
 factors = get_prime(factors)
 for x in factors:
     if product % i != 0:
         product = product * x
     if product % i == 0:
         break
     else:
         product = product/x#multiplying the factors one by one of all the elementsof non prime numbers to make the product a multipe of it
print(product)#printing the answer


 #answer
 #232792560
