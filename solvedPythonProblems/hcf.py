#HCF
numbers = int(input("Kitne numbers do ge:"))
inputs = []

for number in range(numbers):
	inputs.append(int(input('Number:')))
a = max(inputs)
dictionary = {}
for i in range(1,a):
	dictionary[i] = 0
for number in inputs:
	for x in range(1,number//2 + 2):
		if number % x == 0:
			dictionary[x] += 1
factors = []
for i in dictionary:
	if dictionary[i] == len(inputs):
		factors.append(i)
hcf = max(factors)

print("HCF : ",hcf) 
