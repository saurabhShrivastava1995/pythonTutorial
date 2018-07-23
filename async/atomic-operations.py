import time
import random
import queue
from threading import Thread

counter = 0

def update_counter():
	time.sleep(random.random())
	global counter
	time.sleep(random.random())
	counter += 1
	time.sleep(random.random())
	print(f"The value of counter is {counter}")


arr = [Thread(target=update_counter)for x in range(10)]

for i in range(10):
	arr[i].start()


for i in range(10):
	arr[i].join()
	
