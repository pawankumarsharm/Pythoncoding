s="This is ' single quote symbol"
s1='This is "  double quote symbol'
s2='This is "\ double quote symbol'
s3='''These are ' and " symbols'''
print(s)
print(s1)
print(s2)
print(s3)

s="durga"
print(s[0]) #d
print(s[-1]) #a 
#print(s[7])

s4=input("Enter some string:")
i=0
for x in s4:
	print("The character present at positive index:{} and at negative index:{} is :{}".format(i,len(s4)),x)
