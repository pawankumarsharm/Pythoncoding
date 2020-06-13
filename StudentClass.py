class Student:
	'''This class developed by Durga for Demo purpose''' #doc_string
#print(Student.__doc__)
#help(Student)
	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name
	def talk(self):
		print('Hello My Name is:',self.name)
		print('My RollNo is:',self.rollno)
		
s=Student(100,'sunny')
print(s.name)#sunny
print(s.rollno)#100
s.talk()
S1= Student(200,'bunny')
S1.talk()
S3= Student(300,'chinny')
S3.talk()

'''sunny
100
Hello My Name is: sunny
My RollNo is: 100
Hello My Name is: bunny
My RollNo is: 200
Hello My Name is: chinny
My RollNo is: 300'''