class P:
	def m1(self):
		print('parent method')
			
			
class C1(P): 
	def m2(self):
		print('child1 method')
		

class C2(P):
	def m3(self):
		print(' child2 methd')
c=C1()
c.m1()
c.m2()
print()
c1=C2()
c1.m1()
c1.m3()

'''parent method
child1 method

parent method
 child2 methd'''