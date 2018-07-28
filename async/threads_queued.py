import time
import random
import queue
from threading import Thread


counter = 0

counter_queue = queue.Queue()


def increment_manager():
	global counter
	time.sleep(random.random())
	while True:
		increment = counter_queue.get()
		time.sleep(random.random())
		counter += increment
		print(f"The new value of the counter is {counter}")
		counter_queue.task_done()
	time.sleep(random.random())

Thread(target=increment_manager, daemon=True).start()

def increment():
	counter_queue.put(1)

worker_threads = [Thread(target=increment) for x in range(10)]

for thread in worker_threads:
	thread.start()

for thread in worker_threads:
	thread.join()

counter_queue.join()