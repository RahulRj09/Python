
# Sum square difference
# Problem 6
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
natural_square = 0
natural_sum_square = 0
square_list = []
for i in range(1,101):
    square = i ** 2
    square_list.append(square)
natural_square = sum(square_list)

natural_list = []
for i in range(1,101):
    natural_list.append(i)
natural_sum_square = sum(natural_list)**2

print(natural_sum_square-natural_square)

# answer
# 25164150
