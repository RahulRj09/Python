#MDCLXVI
#M = 1000
#D = 500
#C = 100
#L = 50
#X = 10
#V = 5
#I = 1
class romanTOint():
	def __init__(self,roman):
		self.roman = roman
	def romantoint(self):
		roman_list = ['I','V','X','L','C','D','M']
		roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
		roman = self.roman
		if len(roman) == 1:
			return roman + ' : ' + str(roman_dict[roman])
		else:
			sum = 0
			roman = list(roman)
			for numeral in roman:
				if roman.index(numeral) < len(roman)-1:
					next_index = roman.index(numeral)+1
					next_letter = roman[next_index]
					if roman_list.index(numeral) >= roman_list.index(next_letter):
						sum += roman_dict[numeral]
					else: 
						sum -= roman_dict[numeral]
				else:
					sum += roman_dict[numeral]  
			return sum
a = romanTOint('MMMCMLXXXVI')
print(a.romantoint())	
