def gcd(a, b):
    if(b == 0):
        return a
    r = a%b
    return gcd(b,r)

x = 23452
a = 3232*x
b = 14523*x

print(gcd(a, b))
