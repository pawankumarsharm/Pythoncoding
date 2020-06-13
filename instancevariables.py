class Student:
	def __init__(self,name,rollno):
		self.name=name
		self.rollno=rollno
			
	def info(self):
		self.marks=60

s1=Student('durga',101)
s1.info()
s1.age=24 
print(s1.__dict__) #{'name': 'durga', 'rollno': 101, 'marks': 60}

s2=Student('pawan',102)
s2.wife='reshu'
print(s2.__dict__)#{'name': 'pawan', 'rollno': 102, 'wife': 'reshu'}