prompt= "Enter a sentence which may be terminated by either’.’, ‘?’or’!’ only."
prompt += "The words may be separated by more than one blank space and are in UPPER CASE"
vowel=['A','E','I','O','U']
sentence = (input(prompt + "\n>"))
new_sentence = []
new_s = ""
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
	if word[0] in vowel:
		if word[-1] in vowel:
			new_sentence.append(word)
			sentence.remove(word)
print("NUMBER OF WORDS BEGINNIG AND ENDING WITH A VOWEL = " + str(len(new_sentence)))			
for word in sentence:
	new_sentence.append(word)
for word in new_sentence:
	new_s = new_s + word + " "
print(new_s)	

