from pymysql import *
try:
	
	conn=connect("localhost","root","ROOT","abc")
	cursor=conn.cursor()
	cutoff=float(input('Enter cutoff salary'))
	query="delete from employees1 where esal>%f"
	cursor.execute(query %cutoff)	
	conn.commit()
	print('Record deleted successfully')
		
except DatabaseError as e:
	if conn:
		conn.rollback()
		print('there is a problem:',e)
		
finally:
	if cursor:
		cursor.close()
	if conn:
		conn.close()
