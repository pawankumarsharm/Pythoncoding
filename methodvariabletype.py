class Student:
	cname='DURGASOFT'
	def __init__(self,x,y):
		self.name=x
		self.rollno=y
			
	def display(self):
		print('hello Myself is:',self.name)
		print('My RollNo is:',self.rollno)
			
	@classmethod
	def getCollegeName(cls):
		print('College Name:',cls.cname)
			
	@staticmethod
	def findAverage(x,y):
		print('Average:',(x+y)/2)
			
s1=Student('durga',100)
s1.findAverage(10,20)
s1.display()
Student.findAverage(10,20)

'''Average: 15.0
hello Myself is: durga
My RollNo is: 100
Average: 15.0'''