class User():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def greet_user(self):
        print('Hello, ', self.first_name, self.last_name, '!')
        print('How are you doing?')
        
        if input('Type your response') == 'Good':
            print('High5!')
        else:
            print('Hope for the best and cheer up!')
        
    def describe_user(self):
        print('The description if of the person of age', self.age, 'and name', self.first_name , self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        import time
        time.sleep(2)
        print('Attempting to reset login attempts.')
        self.login_attempts = 0
        print('Completed')
    
ankit = User('Ankit', 'Maini', 22)
x = User('X', 'Maini', 20)
ankit.describe_user()
x.greet_user()

ankit.increment_login_attempts()
ankit.increment_login_attempts()
ankit.increment_login_attempts()
ankit.increment_login_attempts()
ankit.increment_login_attempts()
print(ankit.first_name, ' attempted to login ' ,ankit.login_attempts, 'times!')
print('\n\n\n\n\n\n')

if input('Do you wish to reset login attempts? ') == 'Y':
    ankit.reset_login_attempts()
    import time
    time.sleep(2)
    print(ankit.first_name, ' attempted to login ' ,ankit.login_attempts, 'times!')
