filename = 'programming.txt'

# A program that prompts the user for therir name and then writes the name to a file. Append mode!

name = input('Hey! May I know your name, please? :\t')


with open(filename, 'a') as file_object:
    file_object.write('I love programming.\n')
    file_object.write(name)

