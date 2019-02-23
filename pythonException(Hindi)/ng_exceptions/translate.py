
import json

import colorama
from colorama import Fore, Back, Style
colorama.init()


import json
f = open("/ng_exceptions/ng_exceptions/errors.json","r")
s = f.read()
errors = json.loads(s)

def trans_function(word):
	i = 0
	while True:
		if str(errors["values"][i]["from"]) in word:
			error = str(errors["values"][i]["to"]) + "\n"
			error = (Fore.RED + error + Style.RESET_ALL)
			word = word + error
			return  word
		i = i + 1





































# 	if 'NameError' in word:
# 		error = "Naam Truti: Variable define nahi kiya gaya hai"
# 		error = (Fore.RED + error + Style.RESET_ALL)
# 		word = word + error + "\n"
# 		return word
# 	elif 'IndentationError' in word:
# 		error = "Indentation Truti: Apne galat gap diya hai"
# 		error = (Fore.RED + error + Style.RESET_ALL)
# 		word = word + error + "\n"
# 		return word
# 	elif 'TypeError:' in word:
# 		error = "Prakar Truti: Aap galat operation use kar rahe hai"
# 		error = (Fore.RED + error + Style.RESET_ALL)
# 		word = word + error + "\n"
# 		return word
# 	elif 'IndexError:' in word:
# 		error = "Index Truti: List ka index range se zyada hai"
# 		error = (Fore.RED + error + Style.RESET_ALL)
# 		word = word + error + "\n"
# 		return word
# 	elif 'TabError:' in word:
# 		error = "Tab Truti: Tab ya Space ka galat use hua hai"
# 		error = (Fore.RED + error + Style.RESET_ALL)
# 		word = word + error + "\n"
# 		return word
# 	elif 'FileNotFoundError:' in word:
# 		error = "File Not Found Truti: Ye file exist nahi krti hai"
# 		error = (Fore.RED + error + Style.RESET_ALL)
# 		word = word + error + "\n"
# 		return word
# 	elif 'UnsupportedOperation:' in word:
# 		error = "Unsupported Operation Truti: Aapke dwara use kiya operation galat hai"
# 		error = (Fore.RED + error + Style.RESET_ALL)
# 		word = word + error + "\n"
# 		return word
# 	elif 'SyntaxError:' in word:
# 		if ('SyntaxError:' in word) and ('scanning' in word):
# 			error = "Syntax Truti: Line ke end me syntax galat hai"
# 			error = (Fore.RED + error + Style.RESET_ALL)
# 			word = word + error + "\n"
# 			return word
# 		elif ('SyntaxError:' in word ) and ('parentheses' not in word):
# 			error = "Syntax Truti: Syntax galat hai"
# 			error = (Fore.RED + error + Style.RESET_ALL)
# 			word = word + error + "\n"
# 			return word
# 		elif ('SyntaxError:' in word ) and ('parentheses' in word):
# 			error = "Syntax Truti: Aapne bracket nahi lagaya hai"
# 			error = (Fore.RED + error + Style.RESET_ALL)
# 			word = word + error + "\n"
# 			return word
# 	else:
# 		return word
#





























































# def trans_function(word):
# 	if 'NameError' in word:
# 		if 'global name' in word:
# 			word = word.replace("NameError: global name" , "Naam Truti: Variable", 1)
# 			word = word.replace("is not defined" , "paribhaashit nahin hai\n", 1)
# 			return word
# 		else:
# 			word = word.replace("NameError: name" , "Naam Truti: Variable", 1)
# 			word = word.replace("is not defined" , "paribhaashit nahin hai\n", 1)
# 			return word
# 	elif 'IndentationError' in word:
# 		word = word.replace(" IndentationError: unexpected indent" , "Indentation Truti: Aapne galat gap diya hai", 1)
# 		return word
# 	return word
