x=[[10,20,30],[40,50,60],[70,80,90]]
print(x)
print('element row wise:')
for r in x:
	print(r)
print('elements in matrix style:')
for i in range(len(x)):
	for j in range(len(x[i])):
		print(x[i][j],end=' ')
	print()

'''[[10, 20, 30], [40, 50, 60], [70, 80, 90]]
element row wise:
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]
elements in matrix style:
10 20 30
40 50 60
70 80 9'''

#list comprehension

l1=[x*x for x in range(1,11)]
print(l1)#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
