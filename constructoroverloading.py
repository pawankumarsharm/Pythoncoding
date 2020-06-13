class Test:
	def __init__(self):
		print('no-arg argument')
	def __init__(self,a):
		print('one-arg argument')
	def __init__(self,a,b):
		print('two-arg argument')
		
t=Test(10,20)#two-arg argument