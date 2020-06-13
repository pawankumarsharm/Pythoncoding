s='abababa'
sub='ab'
l=len(s)
i=s.find(sub)
#count=0
if i==-1:
	print(sub,'not found in the given string')
while l!=-1:
	
	#count=count+1
	print(sub,'present at index:',i) #’ab’ present at index: 0 2 4
	i=s.find(sub,i+len(sub),l)
	#print('The no. of occurances:',count)
