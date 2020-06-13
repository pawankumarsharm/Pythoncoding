s=input('Enter some string:')#a7b4z3
output=''
for x in s:
	if x.isalpha():
		output=output+x
		previous=x
	else:
		output=output+previous*(int(x)-1)
print(output)

