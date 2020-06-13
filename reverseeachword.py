S=input('Enter some string')
L=S.split()
L1=[]
for word in L:
	L1.append(word[::-L])
Output=' '.join(L1)
Print(output)
