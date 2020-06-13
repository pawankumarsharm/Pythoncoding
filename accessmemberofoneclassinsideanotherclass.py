class Employee:

	def __init__(self,eno,ename,esal):
		self.eno=eno
		self.ename=ename
		self.esal=esal
		
	def display(self):
		print('Employee Number:',self.eno)
		print('Employee Name:',self.ename)
		print('Employee Salary:',self.esal)
		
class Test:
	def modify(emp):
		emp.esal=emp.esal+10000
		emp.display()
		
e=Employee(872425,'Durga',70000)
Test.modify(e)

'''Employee Number: 872425
Employee Name: Durga
Employee Salary: 80000'''