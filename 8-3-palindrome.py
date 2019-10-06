def is_palindrome(string1, string2):
    if (string1 == string2[::-1]):
        return True

string1 = 'abc'
string2 = 'cba'

print(is_palindrome(string1, string2))
    
