# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
def get_max_prime(ulist):#function with a list as an argument
    plist = []#list that will contain prime numbers
    for i in ulist:#looping through ulist
        tlist = []#temporary list
        for x in range(1,i):#looping through each element of ulist to check if that number is prime or not
            if i == 1:
                continue
            elif i%x == 0:
                tlist.append(x)
        if len(tlist) == 1:
            plist.append(i)
    return(max(plist))
number = 600851475143
i = 1
ulist = []
while True:
    if i == int(number ** 0.5):
        break
    elif number % i == 0:
        ulist.append(i)
    i = i + 1
print(get_max_prime(ulist))
#answer
#6857
