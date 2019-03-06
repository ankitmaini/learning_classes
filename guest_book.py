# The program runs a while loop and maintains a log ook for the incoming guests
import datetime
guest = True
i = 0
while guest:
    # Accept the input from the user
    name = input('Hey! Please enter your name to log into the guest book! : ')
    i = i + 1

    if name == 'admin':

        # Ask the user to enter password
        password = input('Enter the password to close logbook : ')

        if password == 'admin1':
            print('Thank you', name.title(), '. The Logbook has been closed and saved.')
            guest = False

    else:
        # Append the input to the file
        with open('logbook.csv', 'a') as logbook:
            adder = str(i)+'\t'+ name.center(20, ' ') + '\t' + str(datetime.datetime.today()) + '\n'
            logbook.write(adder)
        



