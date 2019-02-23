class Validity():
    ''' This is a python class to check the validity of a string of parenthesis '''
    def check(self,string):
        ''' This fuction will check if the string is valid or not. '''
        stack,parenthesis = [] , { '(' : ')' , '{' : '}' , '[' : ']' }
        for sym in string:
            if sym in parenthesis:
                stack.append(sym)
            elif len(stack) == 0 or parenthesis[stack.pop()] != sym:
                return False
            else:
                return len(stack) == 0


string = Validity()
print(string.check("(){}[]"))
print(string.check("()[{)}"))
print(string.check("()"))
