def any_lowercase(s):
    for c in s:
        if c.islower():
            return True
    return False
# check if any of the letters in the string is lowercase

print(any_lowercase('AUObAOUEA'), True)

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
# check if first letter is lowercase

print(any_lowercase1('Try'), False)

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
# return always the string 'True'

print(any_lowercase2('ABC'), type(any_lowercase2('ABC')), 'True', "<class 'str'>")

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
# check if last letter is lower

print(any_lowercase3('abcD'), False)

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
# # check if any of the letters in the string is lowercase

print(any_lowercase4('AUObAOUEA'), True)

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
# return True if all letters are lowercase

print(any_lowercase5('saNa'), False)



