def format_string(string):
    print(string)
    cap_string = string.capitalize()
    print(cap_string)
    casefold_string = string.casefold()
    print(casefold_string)
    center_string = string.center(100,'-')
    print(center_string)
    count_string = string.count('o')
    print(count_string)
    encode_string = string.encode(errors='replace')
    print(encode_string)
    ascii_string = string.isalpha() 
    print(ascii_string)
    string_




string = 'Good Morning Sunshine (on Sunday, 05th of May). Hab #!?$ mächtig Spaß'

format_string(string)
