class Restaurant():
	def __init__(self, name, cuisine_type):
		self.name = name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f'Nume {self.name} bucatarie {self.cuisine_type}')

	def open_restaurant(self):
		print('Open')


restaurant = Restaurant('Marty', 'italian')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_2 = Restaurant('Olivo', 'francez')
restaurant_3 = Restaurant('Meron', 'Spanion')
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()