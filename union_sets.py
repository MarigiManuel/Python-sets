# Union Sets

names = {'Iresa', 'Manuel', 'Marigi'}
subjects = {'Math', 'Comp', 'Stat'}
n_subjects = names.union(subjects)

print(n_subjects)

# Example two

p1 = {'Java', 'JS', 'PHP'}
p2 = {'Python', 'JS', 'PHP'}
p_combined = p1.union(p2)

print(p_combined)

# Example 3

n1 = {1, 2, 3, 4}
n2 = {3, 4, 5, 6}
n = n1.union(n2)

print(n)

# Using | operator

colors1 = {'Red', 'Blue', 'White'}
colors2 = {'Blue', 'Red', 'Black'}
colors = colors1 | colors2

print(colors)

# Unlike the | operator, the union() method accepts one or more iterables, converts the iterables to sets, and performs the union.

rates = {1, 2, 3}
ranks = [2, 3, 4]

ratings = rates.union(ranks)

print(ratings)

# The union operator (|) only allows sets, not iterables like the union() method

rates = {1, 2, 3}
ranks = [2, 3, 4]

ratings = rates | ranks

print(ratings)                  # Output: Error

# Python Intersection
# The intersection of two or more sets returns elements that exist in all sets.

s1 = {'Manuel', 'Iresa', 'Marigi'}
s2 = {'Iresa', 'Chacha', 'Manuel'}
s = s1.intersection(s2)

print(s)

# Using Python set intersection (&) operator to intersect two or more sets

p1 = {'Python', 'Django', 'Pandas'}
p2 = {'Python', 'Pandas', 'Excel'}
p3 = {'SQL', 'Pandas', 'Python'}
p = p1 & p2 & p3

print(p)

# The set intersection operator only allows sets, 
# while the set intersection() method can accept any iterables, like strings, lists, and dictionaries.

s1 = {'Marigi', 2, 3}
s2 = [1, 2, 'Marigi']
s3 = {2, 'Marigi', 'Chacha'}
s = s1.intersection(s2, s3)

print(s)

# Python set difference
# A difference between two sets results in a new set containing elements in the first set that aren’t present in the second set.
# Use the set difference() method or set difference operator (-) to find the difference between sets.

# Using the difference method

values1 = {2, 4, 5, 6}
values2 = {7, 2, 9, 5}
values = values1.difference(values2)

print(values)

fruits1 = {'Oranges', 'Apple', 'Mango'}
fruits2 = {'Apple', 'Grapes', 'Ova'}
fruits = fruits2.difference(fruits1)

print(fruits)

# Using ( - ) difference operator

values1 = {2, 4, 5, 6}
values2 = {7, 3, 4, 5}
values = values1 - values2

print(values)

fruits1 = {'Oranges', 'Ova', 'Mango'}
fruits2 = {'Apple', 'Pineapple', 'Ova'}
fruits = fruits2 - fruits1

print(fruits)

# The set difference() method can accept one or more iterables (e.g., strings, lists, dictionaries) 
# while the set difference operator (-) only allows sets.

# Using the symmetric_difference() method to find the symmetric difference of sets
# The symmetric difference between two sets is a set of elements that are in either set, but not in their intersection.

tech_subj = {'Python', 'Bio', 'Prog'}
non_tech = {'Java', 'Bio', 'Prog'}
subjects = tech_subj.symmetric_difference(non_tech)

print(subjects)

# Using the symmetric difference operator(^) to find the symmetric difference of sets

tech_subj = {'Python', 'Bio', 'Prog'}
non_tech = {'Java', 'Bio', 'Prog'}
subjects = tech_subj ^ non_tech

print(subjects)

# The symmetric difference operator (^) only applies to sets
# The symmetric_difference() method accepts one or more iterables that can be strings, lists, or dictionaries.

# Using subsets

n1 = {1, 2, 3, 4, 5, 6}
n2 = {5, 6, 1}
n = n2.issubset(n1)

print(n)
#####

n1 = {1, 2,}
n2 = {1, 2, 4, 5, 6, 7}
n = n1.issubset(n2)

print(n)

####
n1 = {1, 2,}
n2 = {1, 2, 4, 5, 6, 7}
n = n1 <= n2             # Subset operator

print(n)


# Using Superset
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
s = s1.issuperset(s2)   # False

print(s)
### 

s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
s = s2.issuperset(s1)   # True

print(s)
###

s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
s = s2 >= s1            # Using superset operator

print(s)

# Using disjoint sets
# Two sets are disjoint when they have no elements in common. 
# In other words, two disjoint sets are sets whose intersection is an empty set.
# Use the Set isdisjoint() method to check if two sets are disjoint or not.
# The isdisjoint() method also accepts any iterable, not just a set.

odd_numbers = {1, 3, 5}
even_numbers = {2, 4, 6}
result = odd_numbers.isdisjoint(even_numbers)

print(result)              # True

######
odd_numbers = {1, 3, 5}
even_numbers = {2, 3, 6}
result = odd_numbers.isdisjoint(even_numbers)

print(result)              # False

# Can accept iterables

odd_numbers = {1, 3, 5}
even_numbers = [2, 3, 6]
result = odd_numbers.isdisjoint(even_numbers)

print(result)   
####

odd_numbers = {1, 3, 5}
result = odd_numbers.isdisjoint([1, 3, 5])

print(result)            # False

#####

mixed = {1, 'A', 3, 5}
# result = mixed.isdisjoint([4, 7, 8, 9])         # True
result = mixed.isdisjoint([4, 7, 8, 'A'])         # False

print(result)