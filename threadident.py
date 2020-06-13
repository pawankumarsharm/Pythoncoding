from threading import *
def test():
	print('Child Thread')
	
t=Thread(target=test)
t.start()

print('Main Thread Identification Number:',current_thread().ident)
print('Child Thread Identification Number:',t.ident)

'''Child Thread
Main Thread Identification Number: 21720
Child Thread Identification Number: 15856'''