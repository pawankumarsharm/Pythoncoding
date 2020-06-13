class Person:
	def __init__(self,name,dd,mm,yyyy):
		self.name=name
		self.dob=self.DOB(dd,mm,yyyy)
	def display(self):
		print('Name:',self.name)
		self.dob.display()
		
	class DOB:
		def __init__(self,dd,mm,yyyy):
			self.dd=15
			self.mm=8
			self.yyyy=1947
		def display(self):
			print('DOB={}/{}/{}'.format(self.dd,self.mm,self.yyyy))
			
p=Person('sunny',24,5,2001)
p.display()
p.dob.display()