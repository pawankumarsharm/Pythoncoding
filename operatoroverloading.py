class Book:
	def __init__(self,pages):
		self.pages=pages
	def __add__(self,other):
		return self.pages+other.pages
	def __sub__(self,other):
		return self.pages-other.pages
	def __mul__(self,other):
		return self.pages*other.pages
	def __div__(self,other):
		return self.pages/other.pages
		
b1=Book(100)
b2=Book(200)
b3=Book(300)
print(b1+b2)#300
print(b1+b3)#400
print(b2+b3)#500
print(b1-b2)#-100
print(b1*b2)#20000
print(b1/b2)#unsupported operand type(s) for /: 'Book' and 'Book'
#print(b1+b2+b3)# unsupported operand type(s) for +: 'int' and 'Book'