s=input('Enter Some String:') #---- > ‘durga’
n=len(s)
i=0
print('Data IN Forward Direction:') #-->‘durga’
while i<n:
	print(s[i],end='')
	i=i+1
print()
print('Data in Backward Direction') #’agrud’
i=n-1
while i>=0:
	print(s[i],end='')
	i=i-1
print()
print('Data in Backward Direction with –ve index') #’agrud’
i=n-1
while i>=-n:
	print(s[i],end='')
	i=i-1
