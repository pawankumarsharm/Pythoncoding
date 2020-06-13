for x in range(21):
	if(x%2==0):
		print(x) #0 2 4 6 8 10 12 14 16 18
		
for x in range(10,0,-1):
	print(x) #9 8 7 6 5 4 3 2 1
	
list=eval(input("Enter some list:"))   #10,20,30,40
sum=0
for x in list:
	sum+=x
print("The Sum is", sum)  #the sum is 100
