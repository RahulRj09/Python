a = [1,2,6,3,4,5]
b = []
max = a[0]
c = 4
for i in range(c):
	for i in range(len(a)):
		if max<a[i]:
			max = a[i]
			
	b.append(max)
	d = a.index(max)
	max = a[0]
	a.pop(d)
for i in b:
	print("max number " + str(i))
