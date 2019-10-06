
def squareroot (a, x, epsilon):
    while True:
        print(x)
        y = (x + a/x) / 2
        if abs(y - x) < epsilon:
            break
        x = y

a = 10000000000
x = a / 2
epsilon = 0.00000001

squareroot(a, x, epsilon)
