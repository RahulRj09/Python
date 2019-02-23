# class MyNewClass():
# 	"""This is my new class"""
# 	pass
# print(MyNewClass.__doc__)

class MyClass():
	"This is my second class"
	a = 10
	def func(self):
		return 'Hello'

# print(MyClass.a)
# print(MyClass.func)
# print(MyClass.__doc__)

# creating a new object 
ob = MyClass()
#this is a function of MyClass
print(MyClass.func)
#
print(ob.func)

print(ob.func())