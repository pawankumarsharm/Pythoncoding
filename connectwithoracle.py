from pymysql import *
con=connect("localhost","root","ROOT")
if con!=None:
	print('Connection estaablished successfully')
	#print('Version:'cx_oracle.version)
else:
	print('Connection not established')
con.close()