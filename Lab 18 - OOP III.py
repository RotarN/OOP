class A():
	count = 0
	def __init__(self):
		A.count = A.count + 1

	def describe(self):
		print('Sunt un obiect A')

	@classmethod # acesta este un class method
	def num_instance(cls):
		print(f'Clasa A are {cls.count} instante create')

	@staticmethod
	def metoda_statica():
		#se apeleaza orice
		for i in range (10):
			print(f'valoarea lui {i}')


obj1 = A()
obj2 = A()
A.num_instance()
obj3 = A()
obj4 = A()
obj5 = A()
A.num_instance()
A.metoda_statica()


#  metoda magica
class Word():
	def __init__(self, text):
		self.text = text

	def __eq__(self, word2):
		return self.text.lower() == word2.text.lower()

	def __str__(self):
		return self.text

	def __repr__(self):
		return self.text

ob1 = Word('abc')
ob2 = Word('ABC')
ob3 = Word('xyz')
print(ob1 == ob2)
print(ob1 == ob3)
ob1



class Tail():
	def __init__(self, length):
		self.length = length


class Bill():
	def __init__(self, description):
		self.description = description


class Duck():
	def __init__(self, bill, tail):
		self.bill = bill
		self.tail = tail

	def about(self):
		print(f'Duck has a: {self.bill.description} bill and a {self.tail.length} tail long')


tail = Tail('long')
bill = Bill('orange')
duck = Duck(bill, tail)
duck.about()

from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
ob1 = Duck('wide orange', 'long')
print(ob1)
print(f'cioc {ob1.bill}')
print(f'coada {ob1.tail}')
ob2 = ob1._replace(bill='wide orange', tail='short')
print(ob2)

d = {
	'bill': 'black',
	'tail': 'short'
}

ob2 = Duck(**d)
print(ob2)


from dataclasses import dataclass
@dataclass
class Test:
	name: str


ob1 = Test('Ana')
print(ob1)

@dataclass
class Dice:
	nr_fete: str = 6


ob1 = Dice()
print(ob1.nr_fete)

from dataclasses import dataclass
from collections import namedtuple

from pympler import asizeof

PointNamedTuple = namedtuple('PointNamedTuple', 'x, y, z')


@dataclass
class PointDataClass:
	x:int
	y:int
	z:int


namedtuple_mem = asizeof.asizeof(PointNamedTuple(1, 2, 3))
dataclass_mem =  asizeof.asizeof(PointDataClass(1, 2, 3))
print(f'namedtuple: {namedtuple_mem} bytes,\n dataclass: {dataclass_mem} bytes')





