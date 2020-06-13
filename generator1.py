'''def mygen():
	yield 'A'
	yield 'B'
	yield 'C'
	
g=mygen()
print(type(g))#<class 'generator'>
print(next(g))#A
print(next(g))#B
print(next(g))#C
print(next(g))#StopIteration'''

'''import time
def countdown(num):
	print('Count Down Starting..')
	while num>0:
		yield num
		num=num-1
values=countdown(5)
for x in values:
	print(x)
	time.sleep(3)
print('stop')#5 4 3 2 1 stop'''

#to genarate first n numbers
'''def firstn(num):
	n=1
	while n <= num:
		yield n
		n=n+1
for x in firstn(10):
	print(x)#1 2 3 4 5 6 7 8 9 10'''
	
#to generate fibonacci numbers
'''def fib():
	a,b=0,1
	while True:
		yield b
		a,b=b,a+b

for n in fib():
		if n>100:
			break
		print(n)#1 1 2 3 5 8 13 21 34 55 89'''
		
#people generator:-
import random
import time
names=['sunny','bunny','chinni','vinny']
subjects=['python','java','blckchain']

def people_list(num):
	results=[]
	for i in range(num):
		person={
			'id':i,
			'name':random.choice(names),
			'subject':random.choice(subjects)
			}
		results.append(person)
	return results
	
def people_generators(num):
	
	for i in range(num):
		person={
			'id':i,
			'name':random.choice(names),
			'subject':random.choice(subjects)
			}
		yield person
	
t1=time.process_time() #or time.perf_counter()#because module 'time' has no attribute clock
people=people_list(1000000)
t2=time.process_time()

print('Time taken by list:',t2-t1)
	
t1=time.process_time()
people=people_generators(1000000)
t2=time.process_time()

print('Time taken by generator:',t2-t1)

'''Time taken by list: 2.296875
Time taken by generator: 0.109375'''