def algo(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b + b[-3:]
    else:
        b = b + bin(3 * (n % 3))[2:]
    r = int(b, 2)
    return r


for n in range(1, 1000):
    if algo(n) < 100:
        print(n)

