import re

print('\n')

# Demo data
data = 'Welcome to this course on Regular Expressions! Today\'s date is the 28th of August.'

print(re.search('Welcome', data), '\n')
print(re.search('Welcome', data).group(), '\n')

print(re.findall('e', data), '\n')

# . Period metacharacter is a wild card. Can match any character except new line
print(re.search('.', data).group(), '\n')
print(re.search('t.', data).group(), '\n')
print(re.findall('t.', data), '\n')

# * Asterisk metacharacter matches the preceding character zero or more times
print(re.findall('t*o', data), '\n')
print(re.findall('s*i', data), '\n')

# + Plus metacharacter is similar to the asterisk, but it matches the preceding character one or more times.
print(re.findall('t+o', data), '\n')

# ? Question mark metacharacter matches either zero or one of the preceding character.
print(re.findall('s?i', data), '\n')

# Escape metacharacters (backslash) is used if you for example want to match a literal period or other special characters
print(re.findall('\.', data), '\n')

# Character classes

# [abc] - Brackets, to match multiple characters
print(re.findall('[abc]', data), '\n')

# [0-9] - Brackets with hyphens to set a specific range of characters to match
print(re.findall('[0-9]', data), '\n')
print(re.findall('[a-z]', data), '\n')
print(re.findall('[A-Za-z]', data), '\n')

# \d \w \s - Character class shorthands
print(re.findall('\d', data), '\n') # \d = numerical digits
print(re.findall('\w', data), '\n') # \w = characters part of a word, alphabetical
print(re.findall('\s', data), '\n') # \s = match whitespace characters

print(re.findall('\d+\w+\s', data), '\n') 