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



# Instances as Attributes
# If we continue adding detail to the ElectricCar class, we might notice that we're adding amny attributes tand methods specific to the car's battery. When we see this happening, we can stop and move those attributes and methods to a separate class called Battery as:

class Battery():
    '''A simple attempt to model a battery for an electric car.'''
    def __init__(self, battery_size = 70):
        '''Initialize the battery's attributes.'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''Print a statement describing the battery size.'''
        print('This car has a '+ str(self.battery_size) + '-kWh battery.')

    # A method to report the range of the car based on the battery size
    def get_range(self):
        '''Print a statement about the range this battery provides.'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = 'This car can go approximately ' + str(range)
        message += ' miles on a full charge.'
        print(message)

# Learning Inheritance
# Say we want to make a class ElectricCar
# Since ElectricCar is just a specific kind of car, we can base the # ElectricCar class on the basic Car class
 # Initial Step: Making a simple version of the ElectricCar class which does everything the Car does

class ElectricCar(Car):
     '''Represnts aspects of a car, specific to electric vehicles.'''
     def __init__(self, make, model, year):
         '''Initialize the attributes of the parent class.
         Then initialize the attributes specific to an electric car.'''
        # The super() function is a special function that helps python make connections between the parent and child class. This line tells python to call the __init__() method from ElectricCar's parent class, which gives ElectricCar instance all the attributes of its parent class.      
         super().__init__(make, model, year)
         self.battery  = Battery()

    # Once we have a child class that inherits from a parent class, we can add any new attributes and methods necessary to differentiate the child class from the parent class.
    #  def describe_battery(self):
    #     '''Print the statement describing the battery size.'''
    #     print('The car has a ' +str(self.battery_size)+ '-kWh battery')



    # Overriding methods from the parent class
    # To do this we can define a method in the child class with the # same name as the method we want to override in parent class. 
    # Python thus disregards the method in the parent class and just # pays attention to the method we define in the child class
    # Assume we have a method in the Car class: fill_gas_tank()
    # Since the gas tank is useless in ElectricCar:
    # We define/ override this as follows:
     def fill_gas_tank(self):
        '''Electric cars do not have gas tanks.'''
        print('This car does not need a gas tank.')



my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()