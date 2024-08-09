# Python has functions for creating, reading, updating and deleting files.

# Open a file
myFile = open("myfile.txt", "w")

# Get some info
print("Name: ", myFile.name)
print("Is Closed: ", myFile.closed)
print("Opening Mode: ", myFile.mode)

# Write to file
myFile.write("I am learning python")
myFile.write(" and Java")
myFile.close()

# Append to file
myFile = open("myFile.txt", "a")
myFile.write("My name is lakshit jain")
myFile.close()

# Read from file
myFile = open("myFile.txt", "r+")
text = myFile.read(100)
print(text)
