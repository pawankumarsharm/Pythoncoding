'''import re
pattern=re.compile('python')
print(type(pattern))#<class 're.Pattern'>'''

'''import re
count=0
pattern=re.compile('ab')
matcher=pattern.finditer('abaababa')
for m in matcher:
	count+=1 #count=count+1
	#print('match is available at start index:',match.start())
	print('start:{},end:{},group:{}'.format(m.start(),m.end(),m.group())
print('The number of occurance:',count)

match is available at start index: 0
match is available at start index: 3
match is available at start index: 5
The number of occurance: 3'''

'''import re
matcher=re.finditer('[a-zA-Z]','a7b@k9z')
for m in matcher:
	print(m.start(),'....',m.group())

0 .... a
2 .... b
4 .... k
6 .... z'''

'''import re
matcher=re.finditer('\S','a7b @k9z') 
for m in matcher:
	print(m.start(),'....',m.group())
	
0 .... a
1 .... 7
2 .... b
4 .... @
5 .... k
6 .... 9
7 .... z'''

'''import re
matcher=re.finditer('a*','aabaabbabbaab') 
for m in matcher:
	print(m.start(),'....',m.group())
	
0 .... aa
2 ....
3 .... aa
5 ....
6 ....
7 .... a
8 ....
9 ....
10 .... aa
12 ....
13 ....'''

import re
s=input('Enter pattern to check:')
m=re.search(s,'abaabaaab')
if m!=None:
	print('Match is available')
	print('First occurance with start index:{} and end index:{}'.format(m.start(),m.end()))
else:
	print('full string not matched')
		