from collections import OrderedDict
glossary = OrderedDict()
glossary = {
    'list': 'an ordered arrangement of values which may be of mixed types. A list is mutable.',
    'tuple': 'a tuple is similar to a list, just that it is immutable.',
    'string': ' a collection of letters, written within quotes. Immutable in type.',
    'import': 'a statement used in python to import a module and thereby use its functionality into the present module.',
    'range': 'a generator object that generates a series based on the arguments passed to it.'
}

for word, meaning in glossary.items():
    print('\n',word,':\n\t', meaning, '\n')
