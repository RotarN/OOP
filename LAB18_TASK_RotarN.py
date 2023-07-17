class Bear():
    def eats(self):
        return 'berries'


class Rabbit():
    def eats(self):
        return 'clover'


class Octothorpe():
    def eats(self):
        return 'campers'


print(f'The bear eats {Bear().eats()}.')
print(f'The rabbit eats {Rabbit().eats()}.')
print(f'The octothorpe eats {Octothorpe().eats()}.')




class Laser():
    def does(self):
        return 'disintegrate'


class Claw():
    def does(self):
        return 'crush'


class Smartphone():
    def does(self):
        return'ring'


class Robot:
    def __init__(self, laser: Laser, claws: Claw, smartphone: Smartphone):
        self. laser = laser
        self. claws = claws
        self. smartphone = smartphone

    def does(self):
        print(self. laser. does() + " " + self. claws. does() + " " + self. smartphone. does())


