#This is our superclass
class Car(object):
    '''This is the class docstring.'''
    def __init__(self, year, make, model):
        self.year = str(year)
        self.make = make
        self.model = model
        self.static = 'constant car data'
    def __str__(self):
        '''Formats a nice string.'''
        return 'String representation: %s %s %s' % (self.year, self.make, self.model)
    def printcar(self):
        '''Echoes back the full name of the vehicle.'''
        print('{0} {1} {2}'.format(self.year, self.make, self.model))
        print(self.static) #just to show off an attribute fetch

#This is our subclass; inherits from Car
class Motorcycle(Car):
    pass



