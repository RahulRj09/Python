class RomanToInt():
    '''This is a python class to convert a roman numeral into and integer '''
    def convert(self,roman):
        ''' This function will do the conversion process '''
    	roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        integer = 0
        for i in range(len(roman)):
            if i > 0 and roman_dict[roman[i]] > roman_dict[roman[i-1]]:
                integer += roman_dict[roman[i]] - 2 * roman_dict[roman[i - 1]]
            else:
                integer += roman_dict[roman[i]]
        return integer
integer = RomanToInt()
print(integer.convert('MMMCMLXXXVI'))
