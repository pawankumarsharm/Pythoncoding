from pymysql import *
try:
	
	conn=connect("localhost","root","ROOT","abc")
	cursor=conn.cursor()
	increament=float(input('Enter Increament salary'))
	salrange=float(input('Enter Salary Range:'))
	query="update employees1 set esal=esal+144 where esal<5000"
	cursor.execute(query %(increament,salrange))	
	conn.commit()
	print('Record updated successfully')
		
except DatabaseError as e:
	if conn:
		conn.rollback()
		print('there is a problem:',e)
		
finally:
	if cursor:
		cursor.close()
	if conn:
		conn.close()
