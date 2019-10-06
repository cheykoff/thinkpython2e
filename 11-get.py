string = "aabbbc"
dictionary = dict()
for key in string:
    dictionary[key] = dictionary.get(key,0) + 1 
    # the method 'get' searches for the parameter 'key' 
    # if it is in the dictionary it returns the value of the key
    # if not it returns the default value (in this case 0)
print(dictionary)
