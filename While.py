i = 0

while i < 10:
    print("{}번째 반복입니다".format(i))
    i += 1

example_dictionary = {

    "KeyA": "Value A",
    "KeyB": "Value B",
    "KeyC": "Value C"
}

print("# dictionary's item function")
#print("items():", example_dictionary.items())

for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))