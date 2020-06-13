from threading import *
print(current_thread().getName())
#current_thread().setName('Sunny Leone')
#print(current_thread().getName())
current_thread().name='Durga'
print(current_thread().name)