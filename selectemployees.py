from pymysql import *
try:
	
	conn=connect("localhost","root","ROOT","abc")
	cursor=conn.cursor()
	query="select * from employees1"
	cursor.execute(query)	
	
	row=cursor.fetchone()
	while row is not None:
		print(row)
		row=cursor.fetchone()
	
'''data=cursor.fetchall()
	for each row in data:
		print('Employee Number:',row[0])
		print('Employee Name:',row[1])
		print('Employee salary:',row[2])
		print('Employee Address:',row[3])
		print()
		print()'''
		
'''	n=int(input('Enter the number of required rows:'))
	data=cursor.fetchmany(n)
	#f=open('dbresults.txt','w')
	#f.write(str(data))
	for each row in data:
		print('Employee Number:',row[0])
		print('Employee Name:',row[1])
		print('Employee salary:',row[2])
		print('Employee Address:',row[3])
		print()
		print()'''	

		
except DatabaseError as e:
	if conn:
		conn.rollback()
		print('there is a problem:',e)
		
finally:
	if cursor:
		cursor.close()
	if conn:
		conn.close()
