import math

def mysqrt(a):
    x = a / 2
    while True:
        y = (x + a/x) / 2
        if abs(y - x) < 0.0000001:
            break
        x = y
    return x

def print_header():
    print ('{0:2}{1:20}{2:20}{3:20}'.format(" a", "  mysqrt(a)", "  math.sqrt(a)", " diff"))

def print_table(a, n):
    print_header()
    while a <= n:
        print('{0:2}{1:20}{2:20}{3:20}'.format(a, mysqrt(a), math.sqrt(a),(abs(mysqrt(a) - math.sqrt(a)))))
        a = a + 1

a = 1
n = 9
print_table(a, n)
