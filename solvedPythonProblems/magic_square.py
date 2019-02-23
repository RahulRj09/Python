magic_square = [[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]
rows = []
columns = []
diagonals = []
a,b = 0,0
for i in range(len(magic_square)):
	c_total = 0
	for lst in magic_square:
		if len(rows) < len(magic_square):
			rows.append(sum(lst))
		c_total += lst[i]
	columns.append(c_total)
	for index,lst in enumerate(magic_square):
		a += int(lst[index])
	for index,lst in enumerate(magic_square):
		b += int(lst[::-1][index])
	if len(diagonals) < 2:
		diagonals.append(a)
		diagonals.append(b)
all_tot = []
for i in rows+columns+diagonals:
	if i not in all_tot:
		all_tot.append(i)
print(len(all_tot) == 1)		
