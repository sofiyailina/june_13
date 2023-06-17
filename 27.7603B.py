with open('27B_7603.txt') as f:
    n = int(f.readline())
    k = int(f.readline())
    data = [int(line) for line in f]
maxsum = 0
max_prev = data[0]
for i in range(k, n):
    maxsum = max(maxsum, data[i] + max_prev)
    max_prev = max(max_prev, data[i-k+1])
print(maxsum)
