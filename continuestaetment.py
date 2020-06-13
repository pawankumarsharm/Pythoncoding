for i in range(10):
	if i%2==0:
		continue
	print(i) #1 3 5 7 9

numbers=[10,20,0,5,0,30]
for n in numbers:
	if n==0:
		print("Hey how we can divide with zero…pagal ho gya kya")
		continue
	print('100/{}={}'.format(n,100/n)) #---100/10=10.0  100/20=5.0 hey how we can devide with zero……..
