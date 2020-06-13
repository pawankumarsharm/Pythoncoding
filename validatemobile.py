'''import re
s=input('Enter mobile number to validate:')
m=re.fullmatch('[6-9]\d{9}',s)
if m!=None:
	print(s,'is valid mobile number')
else:
	print(s,'is not vaild mobile number')'''
	
'''import re,urllib
import urllib.request
u=urllib.request.urlopen('https://www.redbus.in/info/contactus')
text=u.read()
numbers=re.findall('[0-9]{3,4}[- ][0-9-]+',str(text))
for n in numbers:
	print(n)'''
	
import re
s=input('Enter Mail id:')
m=re.fullmatch('\w[a-zA-Z0-9_.]*@(gmail|rediffmail)[.][a-z]+',s)
if m!=None:
	print('valid mail Id')
else:
	print('Invalid mail ID')