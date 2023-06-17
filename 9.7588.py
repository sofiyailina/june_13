f = open('9.7588')
k = 0
for s in f:
    a = sorted(int(x) for x in s.split())
    if len(set(a)) == len(a):
        if 3*(a[0] + a[4]) <= 2*(a[1] + a[2] + a[3]):
            k += 1

print(k)