class FirstHundredNumbers():
	def __init__(self):
		self.number = 0
		self.iteration = 0

	def __next__(self):
		if self.iteration < 100:
			current = self.number
			self.number += 1
			return current
		else:
			raise StopIteration()

print(next(FirstHundredNumbers()))
