import math
def estimate_pi():
    k = 0
    addend_series = 1
    sum_series = 0
    while (addend_series >= 1e-15):
        addend_series = math.factorial(4*k)*(1103+26390*k) / (math.factorial(k)**4 * 396**(4*k))
        sum_series = sum_series + addend_series
        k = k + 1
    print("iterations: ", k)
    return 1 / (sum_series * 2 * math.sqrt(2) / 9801)



my_pi = estimate_pi()
print("my_pi: ", my_pi)
print("math.pi: ", math.pi)
print("difference: ", abs(my_pi - math.pi))
