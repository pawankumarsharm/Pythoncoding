class Book:
	def __init__(self,pages):
		self.pages=pages
		
	def __str__(self):
		return 'The No. of pages:'+str(self.pages)
		
	def __add__(self,other):
		total=self.pages+other.pages
		b=Book(total)
		return b
		
	def __mul__(self,other):
		total=self.pages*other.pages
		b=Book(total)
		return b
		
b1=Book(100)
b2=Book(200)
b3=Book(300)
b4=Book(400)
print(b1)
print(b2)
print(b1+b2)
print(b1*b2)
print(b1+b2+b3+b4)
print((b1+b2)*(b3+b4))

'''The No. of pages:100
The No. of pages:200
The No. of pages:300
The No. of pages:2000
The No. of pages:1000
The No. of pages:210000'''