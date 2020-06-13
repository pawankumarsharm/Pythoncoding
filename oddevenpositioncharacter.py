#1st way
s=input('Enter some string')#-durga
print('Characters at Even position:',s[::2])#dra
print('Characters at Odd position:',s[1::2])#ug

#2nd way
s=input('Enter some string') # durga
i=0
print('Characters at Even position:')#d,r,a
while i<len(s):
	print(s[i],end=',')
	i=i+2
print()
i=1
print('Characters at Odd position:')#u,g
while i<len(s):
	print(s[i],end=',')
	i=i+2
