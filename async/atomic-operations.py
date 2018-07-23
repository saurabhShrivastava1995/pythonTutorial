import time
import random
import queue
from threading import Thread

counter = 0

def update_counter():
	global counter
	counter += 1
	print(f"The value of counter is {counter}")

arr = [Thread(target=update_counter)for x in range(10)]

for i in range(10):
	arr[i].start()


for i in range(10):
	arr[i].join()
	
