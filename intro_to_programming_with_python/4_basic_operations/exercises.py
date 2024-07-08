# 1. Concatenate two strings, one with your first name and one with your last, to create a new string with your full name as its value. For example, if your name is John Doe, you should combine 'John' and 'Doe' to get 'John Doe'.

print("James" + " Wallace")


# 2. This question may be a little challenging if your math skills are rusty. Don't be afraid to take advantage of the hints. Try your best to solve the problem, but don't feel compelled to complete it if you become frustrated.

# Use the REPL and the arithmetic operators to extract the individual digits of 4936:

# One place is 6.
# Tens place is 3.
# Hundreds place is 9.
# Thousands place is 4.
# Each digit may require multiple Python statements.

number = 4936
ones = number % 10
tens =  number // 10 % 10
hundreds = number // 100 % 10
thousands = number // 1000 % 10

print(ones)
print(tens)
print(hundreds)
print(thousands)


# 3. What does the following code do? Why?

print('5' + '10')

# Both '5' and '10' are strings.
# When used with string operands, the `+` operator concatenates the srings and returns a new string
# This is is because Python doesn't apply implicit coercion and convert the strings to integers first
# Therefore, this outputs 510


# 4. Refactor the code from the previous exercise to use coercion to print 15 instead.

print(int('5') + int('10'))


# 5. Will an error occur if you try to access a list element with an index greater than or equal to the list's length? For example:

foo = ['a', 'b', 'c']
# print(foo[3])      # will this result in an error?

# This will result in an IndexError because we cannot access an index equal to or greater than the lenth of a list.

# Solution:
# Yes, an error will occur: list index out of range. 
# When you use an index value with no corresponding element, Python raises an IndexError error.


# 6. To what value does the following expression evaluate?

'foo' == 'Foo'

# This expression evaluates to `False`
# Strings are compared lexiographically, which is charater by character.
# 'f' is not equal to 'F', so Python returns False


# 7. What will the following code do? Why?

int('3.1415')

# This will raise a `ValueError` as the string '3.1415' does not represent a valid integer.

# int(3.1415) would return the integer 3.
# The `int` function converts other types, such as a string, to an integer
# The integer returned will have no values after the decimal point.


# 8. To what value does the following expression evaluate?

'12' < '9'

# This expression will evaluate to True
# Strings are compared lexiographically, which is character by character from left to right.
# The character '1' is less than the character '9'
