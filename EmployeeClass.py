class Employee:
	'''doc string(description)'''

	def __init__(self,eno,ename,esal,eaddr):
		self.eno=eno
		self.ename=ename
		self.esal=esal
		self.eaddr=eaddr

	def info(self):
		print('*'*20)
		print('Employee number',self.eno)
		print('Employee Name',self.ename)
		print('Employee Salary',self.esal)
		print('Employee address',self.eaddr)
		print('*'*20)

e1=Employee(100,'Durga',10000,'Hyd')
e2=Employee(200,'pawan',20000,'Chennai')
e1.info()
e2.info()

'''********************
Employee number 100
Employee Name Durga
Employee Salary 10000
Employee address Hyd
********************
********************
Employee number 200
Employee Name pawan
Employee Salary 20000
Employee address Chennai
********************'''
