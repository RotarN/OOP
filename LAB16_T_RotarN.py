# # Task 1

class Thing():
	pass


print(Thing())

example_from_this_class = Thing()

# # Task 2


class Thing2():
	pass

Thing2.letter = 'abc'
print(Thing2.letter)


# # Task 3

class Thing3():
	def __init__(self, name):
		self.name = name
		print(name)

letters = Thing3('xyz')


# Task 4

class Element():
	def __init__(self, name, symbol, number):
		self.name = name
		self.symbol = symbol
		self.number = number

	def show(self):
		print(f'{self.name} {self.symbol} {self.number}')


a = Element('hydrogen', 'H', 1)
a.show()