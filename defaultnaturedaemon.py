from threading import *
import time
'''def job1():
	print('Executed by t1')
	t2=Thread(target=job2)
	print('t2 is Daemon:',t2.isDaemon())
	t2.start()
	
def job2():
	print('Executed by t2')
	
t1=Thread(target=job1)
t1.setDaemon(True)
print('t1 is daemon:',t1.isDaemon())#False
t1.start()
time.sleep(10)'''

def job():
	for i in range(10):
		print('Lazy Thread')
		time.sleep(2)
		
t=Thread(target=job)
t.setDaemon(True)
t.start()
time.sleep(10)
print('End of main thread')