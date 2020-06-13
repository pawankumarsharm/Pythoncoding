n=int(input("Enter the number of rows:"))
for i in range(1,n+1): #i represents row number
	#print('* '*i)#-------optional
	for j in range(1,i+1): #j represents the number of *
		print('*',end=' ')
	print()

n=int(input("Enter the number of rows:"))
for i in range(n):
	for j in range(n):
		print('*',end=' ')
	print()


"""Enter the number of rows:4
*
* *
* * *
* * * *
   Enter the number of rows:3
* * *
* * *
* * *"""