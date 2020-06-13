#to display only even number from the list
list=[1,2,3,4,5,6,7,8,3,4,5,8]
for x in list:
	if x%2==0:
		print(x)
		
#to display element at +ve and -ve index
list=['A','B','C','D','E']
x=len(list)	
for i in range(x):
	print(list[i],'is available at positive index:',i,'and at negative index:',i-x)
