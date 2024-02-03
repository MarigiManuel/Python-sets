# print('We will get there no matter what!')

# Python sets use curly braces.

subjects = {'Math', 'Lit', 'Chem', 'Physics', 'Geo'}

print(subjects)

# The set() function removes duplicate elements

characters = set('letters')

print(characters)

# Getting sizes of a set

numbers = {1, 3, 6, 9, 5, 4}
size = len(numbers)

print(size)

# Checking if an element is in a set

fruits = {'Mangoes', 'Oranges', 'Apple', 'Grapes'}
fruit = 'Apple'

if fruit in fruits:
    print(f'Fruits contain {fruit}')

# Adding elements to a set using add() function.

numbers = {17, 3, 5, 90, 45, 43, 12}
numbers.add('Added')

print(numbers)

# Removing an element from a set

fruits = {'Mangoes', 'Oranges', 'Apple', 'Grapes'}
fruits.remove('Apple')

print(fruits)

# Attempting to remove an element not in the set returns an error.
# To avoid the error, use the in operator to check if the element exists.

fruits = {'Mangoes', 'Oranges', 'Apple', 'Grapes'}
if 'Pineapple' in fruits:
    fruits.remove('Pineapple')

print(fruits)

# Or discard() method

skills = {'Problem solving', 'Software design', 'Python programming'}
skills.discard('Java')

print(skills)


# Returning an element from a set

skills = {'Problem solving', 'Software design', 'Python programming'}
skill = skills.pop()

print(skill)


# To remove all elements from a set, you use the clear() method

skills = {'Problem solving', 'Software design', 'Python programming'}
skill = skills.clear()

print(skill)


# Frozen a set
# To make a set immutable, you use the built-in function called frozenset(). 
# The frozenset() returns a new immutable set from an existing one.
# After that, if you attempt to modify elements of the set, you’ll get an error

skills = {'Problem solving', 'Software design', 'Python programming'}
skills = frozenset(skills)
# skills.add('JS')     # Output: AttributeError: 'frozenset' object has no attribute 'add'

print(skills)


# Looping through elements

skills = {'Problem solving', 'Software design', 'Python programming'}

for skill in skills:
    print(skill)

# To access the index of the current element inside the loop, you can use the built-in enumerate() function.

skills = {'Problem solving', 'Software design', 'Python programming'}
for index, skill in enumerate(skills, 1):
    print(f'{index}: {skill}')