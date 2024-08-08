# Strings in Python are either surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name="Lakshit"
age = 20

#Concatenate
print("hello my name is ",name)

#String formatting

#Arguments by position
print("My name is {name} and i am {age} years old".format(name=name,age=age))

#F-strings
print(f'Hello, my name is {name} and I am {age} years old.')

#String Methods
s='hello world'

#Capitalize String
print(s.capitalize())       

#Make all Upper case
print(s.upper())

#Make all lower case
print(s.lower())

#Swap Case
print(s.swapcase())

#Get length
print(len(s))

#Replace
print(s.replace('world','everyone'))

#Count
sub='h'
print(s.count(sub))

#Starts with
print(s.startswith('hello'))

#Ends with
print(s.endswith('d'))

#Split into a list
print(s.split())

#Find Position
print(s.find('r'))

#Is all alphanumeric
print(s.isalnum())

#Is all alphabetic
print(s.isalpha())

#Is all numeric
print(s.isnumeric())