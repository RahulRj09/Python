# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
def palindrome_chk(number):
    number = list(str(number))
    number_rev = number[::-1]
    if number == number_rev:
        return True
    else:
        return False
list1 = [i for i in range(100,1000)]
list2 = list1[:]
palindrome_list = []
for i in list1:
    for x in list2:
        number = i * x
        result = palindrome_chk(number)
        if result == True:
            palindrome_list.append(number)
print(max(palindrome_list))
#answer
#906609
