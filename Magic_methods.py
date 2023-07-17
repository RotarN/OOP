class Word():
	def __init__(self, text):
		self.text = text

	def __eq__(self, word2):
		return self.text.lower() == word2.text.lower()

	def __str__(self):
		return self.text

	def __repr__(self):
		return  self.text


ob1 = Word('abc')
ob2 = Word('ABC')
ob3 = Word('XYZ')

print(ob1 == ob2)
print(ob1 == ob3)
print(ob1)
ob1
