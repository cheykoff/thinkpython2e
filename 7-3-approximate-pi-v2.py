import math
def estimate_pi():
    k = 0
    total = 0
    while True:
        addend = 2 * math.sqrt(2) / 9801 * math.factorial(4*k)*(1103+26390*k) / (math.factorial(k)**4 * 396**(4*k))
        total = total + addend
        k = k + 1
        if addend < abs(1e-15):
            break
    print("iterations: ", k)
    return 1 / total


my_pi = estimate_pi()
print("my_pi: ", my_pi)
print("math.pi: ", math.pi)
print("difference: ", abs(my_pi - math.pi))
 
