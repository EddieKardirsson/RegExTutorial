import re

print('\n')

# Demo data
data = 'Welcome to this course on Regular Expressions! Today\'s date is the 28th of August.'

print(re.search('Welcome', data), '\n')
print(re.search('Welcome', data).group(), '\n')

print(re.findall('e', data), '\n')

# . Period metacharacter is a wild card. Can match any character except new line
print(re.search('.', data).group(), '´\n')
print(re.search('t.', data).group(), '´\n')
print(re.findall('t.', data), '´\n')

# * Asterisk metacharacter matches the preceding character zero or more times
print(re.findall('t*o', data))
print(re.findall('s*i', data))

# + Plus metacharacter is similar to the asterisk, but it matches the preceding character one or more times.
print(re.findall('t+o', data))

# ? Question mark metacharacter matches either zero or one of the preceding character.
print(re.findall('s?i', data))

# Escape metacharacters (backslash) is used if you for example want to match a literal period or other special characters
print(re.findall('\.', data))