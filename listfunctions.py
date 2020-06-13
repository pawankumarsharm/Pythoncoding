l=[10,20,30,40,10,20,10,10]
target=int(input('Enter the value to search:'))
if target in l:
	print(target,'available and its first occurance is at:',l.index(target))
else:
	print(target,'not available')
