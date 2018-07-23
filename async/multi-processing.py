from multiprocessing import Process


def ask_user():
	name = input("Enter your name : ")


def complex_calculation():
	[x**8 for x in range(1000000)]
	print("Did calculation")




ask_user()
complex_calculation()

process1 = Process(target=ask_user)
process2 = Process(target=complex_calculation)

process1.start()
process2.start()

process1.join()
process2.join()

print("Resource sharing not so easy among different processes")

