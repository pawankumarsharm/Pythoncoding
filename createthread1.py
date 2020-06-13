'''import threading
print('Current Executing Thread:',threading.current_thread().getName()) 
'''

#Creating a Thread without using any class:-
'''from threading import *
def display():
	for i in range(10):
		print('Child thread')
		
t=Thread(target=display) #creation a thread object to execute display()
t.start()

for i in range(10):
	print('Main Thread')'''



#Creating a thread by extending Thread class
'''from threading import *
class MyThread(Thread):
	def run(self):
		for i in range(10):
			print('child Thread')
			
t=MyThread()
t.start()
for i in range(10):
	print('Main thread')'''

#Creating a thread without extending Thread class	
from threading import *
class Test:
	def m1(self):
		for i in range(10):
			print('child Thread-1')
			
obj=Test()
t=Thread(target=obj.m1)
t.start()
for i in range(10):
	print('Main thread')






	
	
	'''Child thread
Main Thread
Main Thread
Main Thread
Main Thread
Main Thread
Child thread
Main Thread
Main Thread
Child thread
Child thread
Main Thread
Child thread
Main Thread
Child thread
Main Thread
Child thread
Child thread
Child thread
Child thread'''