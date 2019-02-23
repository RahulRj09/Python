#program to convert integer to roman numerals using classes
class IntToRoman():
    '''A python class to convert integers to roman numerals'''
    def convert(self, integer):
        ''' This fucntion will to the conversion process '''
        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        romans = ["M","CM","D","CD","C","XC","L","XL","X","IX", "V", "IV","I"]
        roman_numeral = ''
        i = 0
        while  integer > 0:
            for x in range(integer // values[i]):
                roman_numeral += romans[i]
                integer -= values[i]
            i += 1
        return roman_numeral

# Creating object of the class IntToRoman
num = IntToRoman()
print(num.convert(1111))
