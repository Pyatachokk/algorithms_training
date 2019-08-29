a = "3141592653589793238462643383279502884197169399375105820974944592"
b = "2718281828459045235360287471352662497757247093699959574966967627"

# Now works just with number of digits as power of 2
def kar_mul(first, second):
    n = len(first)
    m = len(second)
    if n == 1 or m == 1:
        return int(first) * int(second)
    a = first[:n//2]
    b = first[n//2:]
    c = second[:m//2]
    d = second[m//2:]
    return 10**(n//2 + m//2) * kar_mul(a, c) + 10**(n//2) * kar_mul(a, d) + 10**(m //2) * kar_mul(b, c) + kar_mul(b, d)

first = "234121314312121"
second = "20"
print(kar_mul(first, second), int(first) * int(second))