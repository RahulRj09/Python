length = int(input("Enter the range till where you want to print perfect numbers:\n"))

def perfect_number(length):
    for i in range(1,length+1):
        num = i
        factors = []
        total = 0
        for i in range(1,int(num/2)+1):
            if num % i == 0:
                factors.append(i)
        for i in factors:
            total = total + i
        if total == num:
            print (str(num))


perfect_number(length)
