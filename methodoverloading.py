class Test:
	def m1(self):
		print('no-arg method')
		
	def m1(self,x):
		print('one-arg method')
		
t=Test()
t.m1(10)#one-arg method