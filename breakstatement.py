for i in range(10):
	if i==7:
		print("processing is enough…plz break")
		break	
	print(i) #1 2 3 4 5 6 .....processing is enough…plz break

cart=[10,20,600,70,80,90]
for item in cart:
	if item>500:
		print("sorry we cannot process this order…insurance must be required")
		break	
	print("processing item",item)

"""processing item 10
processing item 20
sorry we cannot process this order…insurance must be required"""