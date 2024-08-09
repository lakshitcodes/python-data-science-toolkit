# A loop is used for iterating over a sequence (that is either a list , a tuple , a dictionary, a set or a string).

people = ["Lakshit", "Rohan", "Rohit", "Kunal"]

# Simple for loop
# for person in people:
#     print(person)


# Break
# for person in people:
#     if person == "Rohit":
#         break
#     print(person)

# Continue
# for person in people:
#     if person == "Rohit":
#         continue
#     print(person)

# range
for i in range(len(people)):
    print(people[i])

for i in range(0, 11, 2):
    print(i)

# While loop execute a set of statements as long as a condition is true.

count = 0
while count <= 10:
    print(count)
    count += 1
