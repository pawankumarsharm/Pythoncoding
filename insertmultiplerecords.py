from pymysql import *
try:
	query="insert into employees1 values(%s,%s,%s,%s)"
	conn=connect("localhost","root","ROOT","abc")
	cursor=conn.cursor()
	
	records=[(200,'sunny',2000.70,'Mumbai'),
                  (300,'Bunny',3000.90,'Delhi'),
                  (400,'chinni',4000.67,'Mumbai')]
	
	cursor.executemany(query,records)
	conn.commit()
	print('Records inserted successfully')
except DatabaseError as e:
	if conn:
		conn.rollback()
		print('there is a problem:',e)
		
finally:
	if cursor:
		cursor.close()
	if conn:
		conn.close()
