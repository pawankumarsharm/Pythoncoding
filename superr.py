class A:
	def m1(self):
		print('A class Method')
class B(A):
	def m1(self):
		print('B class method')
class C(B):
	def m1(self):
		print('C class method')
class D(C):
	def m1(self):
		print('D class method')
class E(D):
	def m1(self):
		super(D,self).m1()
		
e=E()
e.m1()
#C class method