

n, p, q, r = list(map(int, input().split(' ')))
arr = list(map(int, input().split(' ')))

prefix_max_arr = [p*arr[0]]
for i in range(1, n):
    prefix_max_arr.append(max(prefix_max_arr[i-1], p*arr[i]))

suffix_max_arr = [0]*n
suffix_max_arr[n-1] = arr[n-1]*r

for i in range(n-2, -1, -1):
    suffix_max_arr[i] = max(suffix_max_arr[i+1], r*arr[i])

# expression = p*a+q*b+r*c
answer = float('-inf')
for i in range(0, n):
    answer = max(answer, prefix_max_arr[i]+q*arr[i]+suffix_max_arr[i])

print(answer)