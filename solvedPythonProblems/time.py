user = int(input())
s = 3
while True:
	if user < s:
		break 
	user -= s
	s = s * 2
print(s,user)
print(s-user+1)

