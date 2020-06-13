import time
import gc
import sys
class Test:
	def __init__(self):
		print('Object Initialization...')
		
	def __del__(self):
		print('Fullfilling last wish and performing cleanup activities..')


'''gc.disable()
print(gc.isenabled())	
t1=Test()
t1=None
time.sleep(10)
print('End of Application')'''

'''t1=Test()
t2=t1
t3=t2
t4=t3
del t1
time.sleep(10)
print('After deleting t1 object not destroyed')
del t2
del t3
time.sleep(10)
print('still object are not eligible for gc')
time.sleep(10)
del t4
time.sleep(10)
print('End of Application')'''

'''list=[Test(),Test(),Test()]
time.sleep(10)
list=None
time.sleep(10)
print('end of application')'''

'''t1=Test()
print(sys.getrefcount(t1))'''