# Change the elements to lower case

languages = {'ENGLISH', 'SWAHILI', 'KURIA', 'KISII'}
l_languages = set()
for language in languages:
    l_languages.add(language.lower())

print(l_languages)

# Or you can use the built-in map() function with a lambda expression

languages = {'ENGLISH', 'SWAHILI', 'KURIA', 'KISII'}
l_languages = set(map(lambda language: language.lower(), languages))

print(l_languages)

# Using set comprehension

tags = {'Django', 'Pandas', 'Numpy'}
lowercase_tags = {tag.lower() for tag in tags}

print(lowercase_tags)

########

numbers = {23, 1, 2, 4, 6, 78, 54}
desc_numbers = sorted(numbers)

print(f'Numbers changed to descending order: {desc_numbers}')