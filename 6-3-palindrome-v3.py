def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def test_palindrome(word):
    if(type(word) is not str):
        print("please enter a string")
        return
    while(len(word) > 1):
        if first(word) == last(word):
            test_palindrome(middle(word))
            return True
        else:
            return False

word = ""

if(test_palindrome(word)):
    print(word, " is a palindrome")
else:
    print(word, " is not a palindrome")
