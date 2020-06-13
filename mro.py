class P:
	def m1(self):
		print('parent method')
		

class C(P):pass #if child contain same method then child class execute

p=P()
p.m1()
print(P.mro())
	

'''
parent method
[<class '__main__.P'>, <class 'object'>]
'''