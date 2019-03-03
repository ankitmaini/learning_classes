def pizza_make(size, *toppings):
    print('Your order for the pizza of size ' + str(size) + ' is being processed with the toppings: ')
    for topping in toppings:
        print('-' + topping)
