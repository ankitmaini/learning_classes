class Die():
    '''Modelling a die.'''
    def __init__(self, sides = 6):
        self.sides = sides
    

    def roll_die(self):
        from random import randint
        print(randint(1, self.sides))
    

six_side_die = Die(6)
for i in range(10):
    six_side_die.roll_die()
    import time
    time.sleep(2)

