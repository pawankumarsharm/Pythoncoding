class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
		
	def display(self):
		print('name:',self.name)
		print('age:',self.age)
		
class Student(Person):
	def __init__(self,name,age,rollno,marks):
		super().__init__(name,age)
		self.rollno=rollno
		self.marks=marks

	def display(self):
		super().display()
		print('Roll Number:',self.rollno)
		print('Marks:',self.marks)
		
class Teacher(Person):
	def __init__(self,name,age,salary,subject):
		super().__init__(name,age)
		self.salary=salary
		self.subject=subject
		
	def display(self):
		super().display()
		print('Salary:',self.salary)
		print('Subject:',self.subject)
s=Student('Ravi',23,101,90)
p=Teacher('Durga',62,10000,'Python')
s.display()
p.display()

'''name: Ravi
age: 23
Roll Number: 101
Marks: 90
name: Durga
age: 62
Salary: 10000
Subject: Python'''