from pymysql import *
try:
	#query='create table employees1(eno int,ename varchar(10),esal float(10,2), eaadr varchar(10))'
	#query='drop table employees'
	query="insert into employees1 values(100,'durga',1000.50,'hyd')"
	conn=connect("localhost","root","ROOT","abc")
	cursor=conn.cursor()
	cursor.execute(query)
	#print('table created successfully')
	#print('table dropped successfully')
	print('data inserted successfully')
	conn.commit()
except DatabaseError as e:
	if conn:
		conn.rollback()
		print('there is a problem:',e)
		
finally:
	if cursor:
		cursor.close()
	if conn:
		conn.close()
