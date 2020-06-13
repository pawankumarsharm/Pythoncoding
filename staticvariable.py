class Student:
	cname='DurgaSoft' #static variable
	def __init__(self,name,rollno):
		self.name=name #instance variable
		self.rollno=rollno
		
s1=Student('durga',101)
s2=Student('pawan',102)
print(s1.name,s1.rollno,s1.cname)
print(s2.name,s2.rollno,s2.cname)
