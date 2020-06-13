class Student:
	def __init__(self,name,rollno):
		print('constructor execution..')
		self.name=name
		self.rollno=rollno

	def display(self):
		print('method execution..')
		print('Hello myself is:',self.name)
		print('My RollNo is:',self.rollno)

s=Student('durga',100)
s.display()
s.display()
s.display()
s.display()


'''constructor execution..
method execution..
Hello myself is: durga
My RollNo is: 100
method execution..
Hello myself is: durga
My RollNo is: 100
method execution..
Hello myself is: durga
My RollNo is: 100
method execution..
Hello myself is: durga
My RollNo is: 100'''