alpha = {
		'A' : 1,
		'B' : 2,
		'C' : 3,
		'D' : 4,
		'E' : 5,
		'F' : 6,
		'G' : 7,
		'H' : 8,
		'I' : 9,
		'J' : 10,
		'K' : 11,
		'L' : 12,
		'M' : 13,
		'N' : 14,
		'O' : 15,
		'P' : 16,
		'Q' : 17,
		'R' : 18,
		'S' : 19,
		'T' : 20,
		'U' : 21,
		'V' : 22,
		'W' : 23,
		'X' : 24,
		'Y' : 25,
		'Z' : 26,	
	}
list1 = []
list2 = [] 
total=0	
prompt= "Enter a sentence which may be terminated by either’.’, ‘?’or’!’ only."
prompt += "The words should be seperated by one blank space and should be in UPPER CASE"
sentence = (input(prompt + "\n>"))
new = ""
while True:
    if sentence == sentence.upper():
        if sentence[-1] == "." or sentence[-1] == "?" or sentence[-1] == "!":
            break
    else:
    	print("INVALID INPUT")
    	exit()        
    
sentence = sentence.split()
last = sentence.pop()
last = list(last)
last.pop()
for i in last:
    new = new + i
sentence.append(new)        
for word in sentence:
	word = list(word)
	for alphabet in word:
		for key,value in alpha.items():
			if alphabet in key:
				total = total + value
	a="".join(word)
	print (a)
	print(total)
	list1.append(a)
	list2.append(total)
	print (list1,list2)	
	total=0
list3 = sorted(list2)
print(list2)
print(list3)


