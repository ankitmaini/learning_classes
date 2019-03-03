class Car():
    '''A simple attempt to represent a car.'''

    def __init__(self, make, model, year):
        '''Initialize attributes to describe a car.'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name.'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        '''Print a statement showing the car's mileage.'''
        print('This car has ', str(self.odometer_reading), 'miles on it.')

    def update_odometer(self, mileage):
        '''A method to update the mileage and prevent rollback of mileage'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cannot rollback an odometer.')
            
        
    def increment_odometer(self, miles):
        '''Add the given amount to the odometer reading.'''
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2018)
print(my_new_car.get_descriptive_name())

print('\n')

my_used_car = Car('Subaru', 'Outback', 2012)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(3000)
my_used_car.read_odometer()





# Learning Inheritance
# Say we want to make a class ElectricCar
# Since ElectricCar is just a specific kind of car, we can base the # ElectricCar class on the basic Car class
 # Initial Step: Making a simple version of the ElectricCar class which does everything the Car does

class ElectricCar(Car):
     '''Represnts aspects of a car, specific to electric vehicles.'''

     def __init__(self, make, model, year):
         '''Initialize the attributes of the parent class.'''
        # The super() function is a special function that helps python make connections between the parent and child class. This line tells python to call the __init__() method from ElectricCar's parent class, which gives ElectricCar instance all the attributes of its parent class.      
         super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())