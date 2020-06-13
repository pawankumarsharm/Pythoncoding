class Student:
	def setName(self,name):
		self.name=name
		
	def getName(self):
		return self.name
		
	def setMarks(self,marks):
		self.marks=marks
		
	def getMarks(self):
		return self.marks
		
n=int(input('Enter number of Students:'))
for i in range(n):
	name=input('Enter Student name:')
	marks=int(input('Enter Student marks:'))
	s=Student()
	s.setName(name)
	s.setMarks(marks)
	#print(s.name) -->for getting name directly
	print('Hi',s.getName()) #for hiding data behind the method
	print('Your Marks Are:',s.getMarks())
	print('*'*20)
	
	'''Enter number of Students:100
Enter Student name:pawan
Enter Student marks:95
Hi pawan
Your Marks Are: 95
********************'''