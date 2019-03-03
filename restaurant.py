class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name, 'is open!')

    def set_number_served(self, value):
        self.number_served = value
    
    def increment_number_served(self, increment):
        self.number_served += increment

# Creating an instance of Restaurant
restaurant_1 = Restaurant('Taj', 'Indian')

#Testing the methods of the restaurant
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

# Printing the number of customers served: initial value
print(restaurant_1.number_served)

# Updating the customers served from outside the class definition without any special methods
restaurant_1.number_served = 20

# Checking if the assignment worked properly
print('Yes, the customers have been updated to 20' if restaurant_1.number_served == 20 else 'Nope')


# Doing the same thing using a method
restaurant_1.set_number_served(50)
print(restaurant_1.number_served)


# Incrementing the number of customers to the previous call
restaurant_1.increment_number_served(20)
print('Total service = ', restaurant_1.number_served)