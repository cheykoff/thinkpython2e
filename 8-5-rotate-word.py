def rotate_word(string, shift):   
    string = string.lower()
    new_string = ''
    for char in string:
        order = ord(char)
        order = order + shift
        if order + shift > 122: order = order - 26
        char = chr(order)
        new_string = new_string + char
    return new_string

print(rotate_word('IBMBM', -1))
    
