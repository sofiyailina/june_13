with open('27A_7603.txt') as f:
    n = int(f.readline())
    k = int(f.readline())
    nums = [int(line) for line in f]
maxsum = 0
for i in range(len(nums)):
    for j in range(i+k, len(nums)):
        s = nums[i] + nums[j]
        maxsum = max(maxsum, s)

print(maxsum)