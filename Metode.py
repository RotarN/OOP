class A():            #metoda de instanta
	count = 0
	def __init__(self):
		A.count = A.count + 1

	def describe(self):
		print('Sunt un obiect A')

	@classmethod   # aceasta este ,, un class method "
	def num_of_instance(cls):
		print(f'Clasa A are {cls.count} instante create')

	@staticmethod
	def metoda_statica():
		# se apeleaza orice
		print('Apelam metoda statica')
		for i in range(10):
			print(f'valoarea lui {i}')

obj1 = A()
obj2 = A()
A.num_of_instance()
ob3 = A()
obj4 = A()
obj5 = A()
A.num_of_instance()
A.metoda_statica()