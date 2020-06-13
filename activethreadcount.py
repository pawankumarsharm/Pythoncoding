from threading import *
import time
def display():
	print(current_thread().name,'...started')
	time.sleep(3)
	print(current_thread().name,'...ended')
	
print('The number of active Threads:',active_count())
t1=Thread(target=display,name='ChildThread-1')
t2=Thread(target=display,name='ChildThread-2')
t3=Thread(target=display,name='ChildThread-3')
t1.start()
t2.start()
t3.start()
l=enumerate()
for t in l:
	print('Thread name:',t.name)
	print('Thread Identification Number:',t.ident)
	print()
	
time.sleep(10)
l=enumerate()
for t in l:
	print('Thread name:',t.name)
	print('Thread Identification Number:',t.ident)
	print()
	
	'''The number of active Threads: 1
ChildThread-1 ...started
ChildThread-2 ...started
ChildThread-3 ...started
Thread name: MainThread
Thread Identification Number: 1592

Thread name: ChildThread-1
Thread Identification Number: 6092

Thread name: ChildThread-2
Thread Identification Number: 18712

Thread name: ChildThread-3
Thread Identification Number: 15220

ChildThread-1 ...ended
ChildThread-2 ...ended
ChildThread-3 ...ended
Thread name: MainThread
Thread Identification Number: 1592'''