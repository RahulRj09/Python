#make an empty list
numbers=[]
#Ask user for input
print("Enter a number:")
for i in range(20):
    number = int(input(">"))
    numbers.append(number)
#find the max number
max = numbers[0]
for i in range(20):
    if max < numbers[i]:
        max = numbers[i]
#print the maximum number
print("The maximum nummber is " + str(max))
#find the minimum numbers
min = numbers[0]
for i in range(20):
    if min > numbers[i]:
        min = numbers[i]
#print the minimum number
print("The minimum nummber is " + str(min))
#add all the elements of the list
total = 0
for i in range(20):
    total = total + numbers[i]
#print the sum of all the elements of the array
print("The sum of all the elements of the list is " + str(total))
