dictionary = {"name": "Matthew Noh", "Address": "123 ABC Ave, Ramsey", "TEL": "123-456-7890", "zip": 39876}

value = dictionary.get("not exist in the dictionary")
print("Value:", value)

if value == None:
    print("Put the value not exist in the dictionary")

print("name:", dictionary["name"])
print("Address:", dictionary["Address"])

print(dictionary)