l = [10, 20, 20, 10, 10, 30, 50, 10, 20]



# s = str(input("Enter a string:\n"))
# s1= ""
# for i in s:
# 	if " " not in i:
# 		s1 = s1 + i
# s = s1
# print(s)


dict = {}
pair = 0
for i in l:
	#if ord(i) in range(65,91) or ord(i) in range(97,123):
	if i not in dict:
		dict[i] = 1
	else:
		dict[i] = dict[i] + 1
for i in dict:
	a = int(dict[i]/2)
	pair = pair + a
print(pair)
