# 1. Identify the data type or class for each of the following values:

#Value            Type          Class
'True'          # String        str
False           # Boolean       bool
(1, 2, 3)       # Tuple         tuple
1.5             # Float         float
[1, 2, 3]       # List          list
2               # Integer       int
range(5)        # Range         range
{1, 2, 3}       # Set           set
None            # NoneType      NoneType
{'foo': 'bar'}  # Dictionary    dict


# 2. Create a tuple called names that contains several pet names. For instance:

# Name
# Asta
# Butterscotch
# Pudding
# Neptune
# Darwin

names = ('Asta', 'Butterscotch', 'Pudding', 'Neptune', 'Darwin')

print(names)
print(type(names))


# 3. Create a dictionary named pets that contains a list of pet names and the type of animal. For instance:

# Name	Animal
# Asta	dog
# Butterscotch	cat
# Pudding	cat
# Neptune	fish
# Darwin	lizard

pets = {
    'Asta':         'dog',
    'Butterscotch': 'cat',
    'Pudding':      'cat',
    'Neptune':      'fish',
    'Darwin':       'lizard',
}

print(pets)
print(type(pets))