class Student:
	def __init__(self,name,marks):
		self.name=name
		self.marks=marks
		
	def display(self):
		print('Hi',self.name)
		print('Your Marks Are:',self.marks)
		
	def grade(self):
		if self.marks>=60:
			print('First Grade')
		elif self.marks>=50:
			print('Second Grade')
		elif self.marks>=35:
			print('You Got Third Division')
		else:
			print('you Are Failed')

n=int(input('Enter number of Students:'))
for i in range(n):
	name=input('Enter Student name:')
	marks=int(input('Enter Student marks:'))
	s=Student(name,marks)
	s.display()
	s.grade()
	print('*'*20)
	
	'''Enter Student name:suraj
Enter Student marks:65
Hi suraj
Your Marks Are: 65
First Grade
********************
Enter Student name:kajal
Enter Student marks:35
Hi kajal
Your Marks Are: 35
You Got Third Division
********************
Enter Student name:awsaf
Enter Student marks:22
Hi awsaf
Your Marks Are: 22
you Are Failed
********************'''
********************'''
