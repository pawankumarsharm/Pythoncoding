class Animal:
	legs=4
	count=0
	
	def __init__(self):
		Animal.count=Animal.count+1
		
	@classmethod
	def getNoOfObjects(cls):
		print('The number of objects created:',cls.count)
	
	
	@classmethod
	def walk(cls,name):
		print('{} walks with {} legs'.format(name,cls.legs))
		
Animal.walk('Dog')
Animal.walk('Cat')

'''The number of objects created:5
Dog walks with 4 legs
Cat walks with 4 legs'''

a1=Animal()	
a2=Animal()
a3=Animal()		
a4=Animal()
a5=Animal()
Animal.getNoOfObjects()