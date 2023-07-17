class Tail():
	def __init__(self, lenght):
		self.lenght = lenght


class Bill():
	def __init__(self, description):
		self.description = description

class Duck():
	def __init__(self, bill, tail):
		self.bill = bill
		self.tail = tail

	def about(self):
		print(f'Duck has a :{self.bill.description} bill and a {self.tail.lenght} tail long')


tail = Tail('Long')
bill = Bill('orange')
duck = Duck(bill, tail)
duck.about()