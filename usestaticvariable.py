class Test:
	a=10
	def __init__(self):
		Test.b=20
	def m1(self):
		Test.c=30
		
	@classmethod
	def m2(cls):
		cls.d=40
		Test.e=50
		
	@staticmethod
	def m3():
		Test.f=60

t=Test()
t.m1()
Test.m2()
Test.m3()

Test.g=70
print(Test.__dict__)#a=10, g=70 only because object not created for other but after creating object you can print all.

