class Outer:
	def __init__(self):
		print('Outer class object creation...')
		
	def m2(self):
			print('Outer class method')
		
	class Inner:
		def __init__(self):
			print('Inner class object creation...')
			
		def m1(self):
			print('Inner class method')
			
o=Outer()
i=o.Inner()
i.m1()
o.m2()
#i=Outer().Inner()
#Outer().Inner().m1()