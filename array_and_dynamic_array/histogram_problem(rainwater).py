# cook your dish here
n = int('6')
arr = list(map(int, '4 2 0 3 2 5'.split(' ')))

prefix_max_arr = [arr[0]]
for i in range(1, n):
    prefix_max_arr.append(max(arr[i], prefix_max_arr[i-1]))

suffix_max_arr = [0]*n
suffix_max_arr[n-1] = arr[n-1]
for i in range(n-2, -1, -1):
    suffix_max_arr[i] = max(suffix_max_arr[i+1], arr[i])
    
answer = 0
for i in range(1, n-1):
    deciding_height = min(prefix_max_arr[i-1], suffix_max_arr[i+1])
    if deciding_height < arr[i]:
        pass
    else:
        answer += deciding_height - arr[i]

print(answer)