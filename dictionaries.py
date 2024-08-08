# A dictionary is a collection which is unordered,changeable and indexed. No duplicate members.

# Create dictionary
person = {
    'first_name' : 'Lakshit',
    'last_name' : 'Jain',
    'age' : 20,
}

#Constructor
person2 = dict(first_name="Lakshit",second_name="Jain",age=20)

#Get Value
# print(person['first_name'])
# print(person.get('last_name'))

# Add key value
person['phone'] = 95625195621

# Get dict keys
# print(person.keys())

# Get dict values
# print(person.values())


# Get dict items
# print(person.items())

# Copy dict
person3 = person.copy() #Deep copy
person4 = person        #Shallow copy

# Remove an item 
del(person['age'])
person.pop('phone')

# Clear the dict
person.clear()

# Get the length
print(len(person3))

# List of dictionaries
people = [
    {'name' : "Kunal", 'age' : 19},
    {'name' : "Lakshit", 'age' : 20},
    {'name' : "Lakshay", 'age' : 20},
]