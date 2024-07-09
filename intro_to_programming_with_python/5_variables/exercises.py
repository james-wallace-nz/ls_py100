# 1. Classify the following potential non-constant variable names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.

# Name
# index             idiomatic
# CatName           non-idiomatic   - should not use capital letters
# lazy_dog          idiomatic
# quick_Fox         non-idiomatic   - should not use capital letters
# 1stCharacter      illegal         - cannot start with a digit
# operand2          idiomatic
# BIG_NUMBER        non-idiomatic   - should not use capital letters
# π                 non-idiomatic   - not an ASCII character


# 2. Classify the following potential function names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.

# Name
# index             idiomatic
# CatName           non-idiomatic
# lazy_dog          idiomatic
# quick_Fox         non-idiomatic
# 1stCharacter      illegal
# operand2          idiomatic
# BIG_NUMBER        non-idiomatic
# π                 non-idiomatic   - not an ASCII character


# 3. Classify the following potential constant names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.

# Name
# index             non-idiomatic   - should not use lowercase letters
# CatName           non-idiomatic   - should not use lowercase letters
# snake_case        non-idiomatic   - should not use lowercase letters
# LAZY_DOG3         idiomatic
# 1ST               illegal         - should not start with a digit
# operand2          non-idiomatic   - should not use lowercase letters
# BIG_NUMBER        idiomatic
# Π                 non-idiomatic   - not an ASCII character


# 4. Classify the following potential class names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.

# Name
# index             non-idiomatic   - should not stat with a lowercase letter
# CatName           idiomatic
# Lazy_Dog          non-idiomatic   - should not have an underscore
# 1ST               illegal         - should not start with a digit
# operand2          non-idiomatic   - should not start with a lowercase letters
# BigNumber3        idiomatic
# Πi                non-idiomatic   - not an ASCII character


# 7. What happens when you run the following code? Why?

# 1. NAME = 'Victor'
# 2. print('Good Morning, ' + NAME)
# 3. print('Good Afternoon, ' + NAME)
# 4. print('Good Evening, ' + NAME)

# On line 1, the constant `NAME` is initialized to the string `'Victor'`.
# Lines 2-4 output the greeting strings concatenated with the `NAME` constant, which is the string 'Victor' 

# 5. NAME = 'Nina'
# 6. print('Good Morning, ' + NAME)
# 7. print('Good Afternoon, ' + NAME)
# 8. print('Good Evening, ' + NAME)

# On line 5, the constant `NAME` is reassigned to the string `'Nina'`. Python allows this reassignment
# even though the convention is to treat `NAME` as a constant.
# Lines 6-8 output the greeting strings concatenated with the `NAME` constant, which is the string 'Nina' 


# 8. Challenge: This program uses a bit of math. Don't let that scare you away -- try it anyway.

# Assume you have $1,000.00 in the bank, and you've somehow managed to find a bank that pays you 5% 
# (this is a wish-fulfillment fantasy) compounded interest every year. After one year, you will have 
# $1,050 ($1,000 times 1.05). After two years, you will have $1,050 times 1.05, or $1102.50. 
# Create a variable named balance that contains the amount of money you will have after 5 years, 
# then print the result. Use a single expression if you can to set balance to the correct value.

balance = 1000 * (1 + .05)**5
print(balance)


# 9. Repeat the previous question but, this time, use augmented assignment to compute the 
# final result, one year at a time.

balance = 1000
balance *= 1.05  # year 1
balance *= 1.05  # year 2
balance *= 1.05  # year 3
balance *= 1.05  # year 4
balance *= 1.05  # year 5

print(balance)


# 10. Assume that obj already has a value of 42 when the code below starts running. 

# Which of the subsequent statements reassign the variable? 
# Which statements mutate the value of the object that obj references? 
# Which statements do neither? If necessary, you can read the documentation.

# obj = 42                  initial assignment

# obj = 'ABcd'              reassignment
# obj.upper()               neither
# obj = obj.lower()         reassignment
# print(len(obj))           neither
# obj = list(obj)           reassignment
# obj.pop()                 mutation
# obj[2] = 'X'              mutation
# obj.sort()                reassignment - ACTUALLY MUTATION SORT DOES MUTUATE
# set(obj)                  neither
# obj = tuple(obj)          reassignment

# Solution:

# A simple assignments like var = something is always either an initialization or 
# a reassignment. Since obj has already been initialized (it has a value of 42 before 
# this code was reached), lines 1, 3, 5, and 10 perform reassignment. 

# In a few situations, mutation and reassignment can happen in the same statement. 
# None of the above statements do both.

# obj.upper does not mutate the caller, so line 2 does neither. 
# Likewise, since print, len, and set don't mutate their arguments, lines 4 and 9 are neither.

# The remaining statements all mutate the object referenced by obj. 
# pop removes the last element of the list. 
# obj[2] = 'X' reassigns the element at index 2, but it mutates obj itself. 
# Finally, sort mutates the object when it performs an in-place sort.
