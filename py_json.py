# JSON is commonly used with data APIs. Here is how we can parse JSON into a python dictionary.

import json

# Sample JSON
userJSON = '{"first_name": "Lakshit","last_name":"Jain", "age" : 20}'

# Parse to dictionary
user = json.loads(userJSON)

# print(user)
# print(user["first_name"])

car = {"make": "Bugatti", "model": "tourbillon", "year": 2024}

carJSON = json.dumps(car)
