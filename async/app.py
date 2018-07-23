import time
from concurrent.futures import ThreadPoolExecutor 

def ask_user():
	name = input("Enter your name : ")


def complex_calculation():
	[x**8 for x in range(1000000)]

start = time.time()
ask_user()
complex_calculation()

print(f'The total time taken for excution of two complex functions : {time.time() - start}')

start = time.time()

with ThreadPoolExecutor(max_workers=2) as pool:
	pool.submit(ask_user)
	pool.submit(complex_calculation)


print(f'The total time taken for execution of both the threads are {time.time() - start}')