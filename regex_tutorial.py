import re

print('\n')

# Demo data
data = 'Welcome to this course on Regular Expressions! Today\'s date is the 28th of August.'

print(re.search('Welcome', data), '\n')
print(re.search('Welcome', data).group(), '\n')

print(re.findall('e', data), '\n')