s='durgasoftdurgasoft'
print(s.count('soft'))#2
print(s.count('soft',8,len(s))) #1

s='Learning python is very difficult'
s1=s.replace('difficult','easy')
print(s1)#--

S='abababa'
S1=s.replace('a','b')
print(s, 'Address is:',id(s)) # abababa Address is :35074560
print(s1,'Address is:',id(s1))#bbbbbbb Address is 35074368

s='Durga Software Solutions'
l=s.split()
print(type(l))
print(l)# ---- >['Durga' , Software' , 'Solutions']
for x in l:
	print(x)#- Durga Software Solutions

s='02—3-2021'
l=s.split('-')
print(l)#['02-3','2021']

s='Durga Software Solutions hyd india'
l=s.rsplit(',',-1)
for x in l:
	print(x)
	
l=['durga','soft','solutions']
s='-'.join(l)
print(s)  

s='The Pyhton Classes By Durga Sir'
print(s.upper()) #THE PYTHPON CLASSES BY DURGA SIR
print(s.lower()) #the python classes by durga sir
print(s.swapcase())# tHE pYTHON cLASSES bY dURGA sIR 
print(s.title()) # The Pyhton Classes By Durga Sir
print(s.capitalize()) #The Pyhton Classes By Durga Sir	

s='Learning Python is very easy'
print(s.startswith('Learning'))#True
print(s.endswith('easy')) #True  


