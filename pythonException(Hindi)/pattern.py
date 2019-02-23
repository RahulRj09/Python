a = 5
for i in (1,a+1):
    if i == 1 or i == a:
        print(a*"*")
    else:
        print("*"+(a-2)*" "+"*")
