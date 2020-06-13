class Test:
	a=10
	def __init__(self):
		print('Inside Constructor')
		print(Test.a)
		print(self.a)
	def m1(self):
		print('Inside instance method')
		print(Test.a)
		print(self.a)

	@classmethod
	def m2(cls):
		print('Inside classmethod')
		print(Test.a)
		print(cls.a)
               
	@staticmethod
	def m3():
		print('inside static method')
		print(Test.a)
t=Test()
t.m1()
t.m2()
t.m3()
print('from outside of the class')
print(Test.a)
print(t.a)   

'''Inside Constructor
10
10
Inside instance method
10
10
Inside classmethod
10
10
inside static method
10
from outside of the class
10
10'''  
