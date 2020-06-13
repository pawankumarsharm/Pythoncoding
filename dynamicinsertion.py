from pymysql import *
try:
	
	conn=connect("localhost","root","ROOT","abc")
	cursor=conn.cursor()
	while True:
		eno=int(input('Enter Employee Number'))
		ename=(input('Enter Employee Name'))
		esal=float(input('Enter Employee Salary'))
		eaddr=input('Enter Employee Address')
		query="insert into employees1 values(%d,'%s',%f,'%s')"
		cursor.execute(query %(eno,ename,esal,eaddr))	
		conn.commit()
		print('Record inserted successfully')
		option=input('do you want to input one more record[yes|no]:')
		if option =='no':
			print('thanks for using my application')
			break

		
	
except DatabaseError as e:
	if conn:
		conn.rollback()
		print('there is a problem:',e)
		
finally:
	if cursor:
		cursor.close()
	if conn:
		conn.close()
