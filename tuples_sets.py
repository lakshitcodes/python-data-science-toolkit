# A tuple is a collection which is ordered and unchangeable. Allows duplicate numbers.

# Create tuple
fruits = ('Apples' ,'Oranges','Grapes')
# Using constructor
fruits2 = tuple(('Apples' ,'Oranges','Grapes'))
# Single value needs trailing comma
fruits3 = ('Apple',)
# print(fruits3,type(fruits3))

# Delete a tuple
del fruits2

#Get length
print(len(fruits))

# A set is a collection which is unordered and unindexed. No duplicate members.

#Create set
fruits_set = {'Apples', 'Oranges','Mango'}

# Check if something is in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Clear set
fruits_set.clear()
# Clearing a set is different from deleting
# Deleting a set completely removes it from the memory
# Clearing only empties the set but the set still exists in memory though empty

# Delete
del fruits_set

