from threading import *
import time
def display():
	print(current_thread().name,'...started')
	time.sleep(3)
	print(current_thread().name,'...ended')
	
t1=Thread(target=display,name='ChildThread-1')
t2=Thread(target=display,name='ChildThread-2')

t1.start()
t2.start()
print(t1.name,'is Alive :',t1.isAlive())
print(t2.name,'is Alive :',t2.isAlive())
time.sleep(10)
print(t1.name,'is Alive',t1.isAlive())
print(t2.name,'is Alive',t2.isAlive())

'''ChildThread-1 ...started
ChildThread-2 ...started
C:\Users\bikram chandra\AppData\Local\Programs\Python\Python38-32\alivethread.py:13: DeprecationWarning: isAlive() is deprecated, use is_alive() instead
  print(t1.name,'is Alive :',t1.isAlive())
ChildThread-1 is Alive : True
C:\Users\bikram chandra\AppData\Local\Programs\Python\Python38-32\alivethread.py:14: DeprecationWarning: isAlive() is deprecated, use is_alive() instead
  print(t2.name,'is Alive :',t2.isAlive())
ChildThread-2 is Alive : True
ChildThread-1 ...ended
ChildThread-2 ...ended
C:\Users\bikram chandra\AppData\Local\Programs\Python\Python38-32\alivethread.py:16: DeprecationWarning: isAlive() is deprecated, use is_alive() instead
  print(t1.name,'is Alive',t1.isAlive())
ChildThread-1 is Alive False
C:\Users\bikram chandra\AppData\Local\Programs\Python\Python38-32\alivethread.py:17: DeprecationWarning: isAlive() is deprecated, use is_alive() instead
  print(t2.name,'is Alive',t2.isAlive())
ChildThread-2 is Alive False'''