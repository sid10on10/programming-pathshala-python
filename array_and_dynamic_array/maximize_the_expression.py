# brute force

p, q, r = [1, 2, 3]


arr = [1,2,3,4,5]
n = len(arr)
# expression = -2*a + 5*b + -3*c

prefix_max = [ 4*-2 ]

for i in range(1, n):
    prefix_max.append(max(prefix_max[i-1], p*arr[i]))

print(prefix_max)


suffix_max = [0]*n
suffix_max[n-1] = r*arr[n-1]

for i in range(n-2, -1, -1):
    suffix_max[i] = max(suffix_max[i+1], r*arr[i])

print(suffix_max)

# for i < j < k
answer = -2**31
for i in range(1, n-1):
    answer = max(answer, prefix_max[i-1] + q*arr[i] + suffix_max[i+1])

print(answer)

# for i <= j <= k
answer = -2**31
for i in range(0, n):
    answer = max(answer, prefix_max[i] + q*arr[i] + suffix_max[i])

print(answer)