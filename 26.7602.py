with open('26_7602.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    #data = [[int(k) for k in line.split()] for line in f ]
    data = []
    for line in f:
        a, b = line.split()
        pair = [int(a), int(b)]
        data.append(pair)
data.sort()
cells = [0] * k
count = 0
last = 0
for t0, t1 in data:
    for i in range(k):
        if cells[i] < t0:
            cells[i] = t1
            count += 1
            last =i + 1
            break
print(count, last)