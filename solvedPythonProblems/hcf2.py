a = int(input())
b = int(input())
factor_list1 = [x for x in range(1,a) if a % x == 0]
factor_list2 = [x for x in range(1,b) if b % x == 0]
print(factor_list1)
print(factor_list2)
fl = []
for x in factor_list1:
	if x in factor_list2:
		fl.append(x) 
print('HCF : ',max(fl))
