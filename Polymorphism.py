class quote():
	def __init__(self, person, words):
		self.person = person
		self.words = words

	def who(self):
		return self.person

	def says(self):
		return self.words + '.'


class question_quote(quote):
	def says(self):
		return self.words + '?'


class exclamation_quote(quote):
	def says(self):
		return self.words + '!'


class B():
	def who(self):
		return 'Clasa simpla '

	def says(self):
		return ' output : clasa simpla'


class x():
	def who(self):
		return ' Clasa X'


def who_says(obj):
	print(f'{obj.who()} says {obj.says()}')


base = quote('Traian Basescu', 'Iarna nu-i ca vara')
who_says(base)
cezar = question_quote('Cezar', 'si tu , Brutus')
who_says(cezar)
anonim = exclamation_quote('Anonim', 'Esti mai catolic ca Papa')
who_says(anonim)

obiect = B()
who_says(obiect)

obiect_x = x()
who_says(obiect_x)