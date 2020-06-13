class Test:
	def m1(self):
		def sum(a,b):
			print('first Argument:',a)
			print('second Argument:',b)
			print('The Sum:',a+b)
			print('The Product:',a*b)
			print('*'*20)
			
		sum(10,20)
		sum(100,200)
		sum(1000,2000)
		
t=Test()
t.m1()