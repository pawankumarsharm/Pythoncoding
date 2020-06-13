class P:
		def property(self):
			print('cash+land+gold+power')
			
		def marry(self):
			print('subbalaxmi')
			
class C(P):
	def marry(self):
		super().marry()
		print('Katrina..')
		
c=C()
c.property()
c.marry()

'''cash+land+gold+power
subbalaxmi
Katrina..'''