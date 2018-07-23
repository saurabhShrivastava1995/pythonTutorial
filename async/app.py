import time
from threading import Thread 

def ask_user():
	name = input("Enter your name : ")


def complex_caluculation():
	[x**8 for x in range(100000000)]

start = time.time()
complex_caluculation()
complex_caluculation()

print(f'The total time taken for excution of two complex functions : {time.time() - start}')


thread1 = Thread(target=complex_caluculation)
thread2 = Thread(target=complex_caluculation)

start = time.time()

thread1.start()
thread2.start()


thread1.join()
thread2.join()

print(f'The total time taken for execution of both the threads are {time.time() - start}')