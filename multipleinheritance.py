class P1:
	def m1(self):
		print('parent1 method')
			
			
class P2: 
	def m1(self):
		print('parent2 method')
		

class C(P1,P2):pass #if child contain same method then child class execute

c=C()
c.m1()
	

'''parent1 method'''