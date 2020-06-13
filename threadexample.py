import time
from threading import *
def doubles(numbers):
	for n in numbers:
		time.sleep(1)
		print('Double values:',2*n)
		
def squares(numbers):
	for n in numbers:
		time.sleep(1)
		print('Square values:',n*n)
		
numbers=[1,2,3,4,5,6]
begintime=time.time()
t1=Thread(target=doubles,args=(numbers,))
t2=Thread(target=squares,args=(numbers,))
t1.start()
t2.start()

t1.join()
t2.join()
endtime=time.time()
print('The total time taken:',endtime-begintime)

'''Square values: 1
Double values: 2
Square values: 4
Double values: 4
Square values: 9
Double values: 6
Square values: 16
Double values: 8
Square values: 25
Double values: 10
Square values: 36
Double values: 12
The total time taken: 6.009063720703125'''