class Test:
	def m1(self):
		global x
		x=888
		print(x)#888

	def m2(self):
		print(x)#888

t=Test()
t.m1()
t.m2()   
