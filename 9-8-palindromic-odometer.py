def is_palindromic(number):
    str_number = str(number)
    if str_number == str_number[::-1]:
        return True
    else: return False

def find_palindrome():
    i = 1
    end = 1000000
    count = 0
    while i < end:
        if is_palindromic(str(i)):
            if is_palindromic(str(i-1)[1:5]):
                if is_palindromic(str(i-2)[1:]):
                    if is_palindromic(str(i-3)[2:]):
                        count = count + 1
                        print(i - 3, i - 2, i - 1, i)
        i = i + 1
    print(count)

find_palindrome()
