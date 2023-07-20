class Cat():
	def __init__(self, name):
		self.name = name
		print('O noua instanta Cat s-a creat', name)


a_cat = Cat('Grumpy')  # prima instanta de tipul Cat
print(a_cat.name)
another_Cat = Cat('Another Grumpy') # a doua instantade tipul Cat


print(a_cat)
print(another_Cat)
# a_cat.age = 3
# a_cat.name = 'Ms Sweet'
# a_cat.link_cat = another_Cat
#
# print(a_cat.age)
# print(a_cat.name)
# print(a_cat.link_cat)
class Car():
	def __init__(self, colour):
		self.colour = colour
	def exclaim(self):
		print("I'm a car")

	def checkColour(self):
		print(f'My colour is {self.colour}')

class Yugo(Car):
	def exclaim(self):
		super().exclaim()    # pastreaza de la parinte
		print(f" I'm a Yugo car")


a_simple_car = Car('negru')
a_simple_car.checkColour()
a_simple_car.exclaim()

a_yugo_car = Yugo('albastru')
a_yugo_car.checkColour()
a_yugo_car.exclaim()


class Person():
	def __init__(self, name):
		self.name = name


class Doctor(Person):
	def __init__(self, name):
		self.name = 'Dr.' + name


class Inginer(Person):
	def __init__(self, name):
		self.name = 'Ing.'+name
	def prezentare(self):
		print(f"{self.name} Inger de profesie")


class EmailPerson(Person):
	def __init__(self,name, email):
		super().__init__(name)
		self.email = email



person = Person("Ion Popescu")
personwithemail = EmailPerson("Ioana Simon ", "ioanasimon@business.ro")
doctor = Doctor("Marin Ionescu")
ing = Inginer("Marius Petrescu")

ing.prezentare()
doctor.prezentare()  # de la copii nu merg atribute la parinti


print(person.name)
print(doctor.name)
print(ing.name)
