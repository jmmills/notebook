# This is our superclass


class Car(object):
    """this is the class docstring."""
    def __init__(self, year, make, model):
        self.year = str(year)
        self.make = make
        self.model = model
        self.static = 'constant car data'

    def __str__(self):
        """Formats a nice string."""
        return 'String representation: {0} {1} {2}'.format(
            self.year, self.make, self.model
        )

    def printcar(self):
        """Echos back the full name of the vehicle."""
        print('{0} {1} {2}'.format(
            self.year, self.make, self.model
        ))


class Motorcycle(Car):

    def wheelie(self):
        pass



ns = Car('1990', 'Nissan', 'Sentra')
str(ns)

print(ns)
print(ns.static)

ns.printcar()
