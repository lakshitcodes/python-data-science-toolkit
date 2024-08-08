# A list is a collection which is ordered and changeable. Allows duplicate numbers.

#Create list
numbers = [1,2,3,4,5]
fruits = ['Apples','Oranges','Grapes','Pears']

# Use a constructor
# numbers2 = list((1,2,3,4,5))

#Get a value
print(fruits[1])

#Get length
print(len(fruits))

# Append to list
fruits.append("Mangoes")

#Remove from list
fruits.remove("Oranges")

#Insert into position
fruits.insert(2,"Strawberries")

#Remove with pop
fruits.pop(3)

#Reverse the list
fruits.reverse()

#Sort alphabetically
fruits.sort()

#Reverse Sort
fruits.sort(reverse=True)

print(fruits)