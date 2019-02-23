num = 21
original_list = [n for n in range(1,num+1)]
duplicate_list = original_list[:]
final_list = []
i = 1
while duplicate_list != []:
	temp_list = []
	for x in range(i):
		#print(x)
		popped = duplicate_list.pop(0)
		temp_list.append(popped)
	final_list.append(temp_list)
	i += 1

for x,lis in enumerate(final_list):
	if x%2 == 0:
		for i,x in enumerate(lis):
			if i != len(lis)-1:
				print(x,end = ' ')
			else:
				print(x)
	else:
		lis = lis[::-1]
		for i,x in enumerate(lis):
			if i != len(lis)-1:
				print(x,end = ' ')
			else:
				print(x)
