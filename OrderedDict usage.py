# The dictionaries don't keep track of the oreder in which the key-value pairs are added. So, in order to track the order in which the key value pairs are added, we use OrderedDict class from collections module
from collections import OrderedDict
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + '\'s favorite language is ' + language.title() +'.')