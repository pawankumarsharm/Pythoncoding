s=input('Enter Main String')#durgasoftdurgasoft
subs=input('Enter substring:')
flag=False
pos=-1
n=len(s)
count=0
while True:
	pos=s.find(subs,pos+1,n)
	if pos==-1:
		break
	print('found at index:',pos)
	flag=True
	count=count+1
if flag==False:
	print('Not Found:')
print('No of occurances :',count)#2
