arr = [4, 70, -3, 54, 17, 49, 12, 45]

# prefix sum array
prefix_sum_arr = [arr[0], ]
for i in range(1, len(arr)):
    prefix_sum_arr.append(prefix_sum_arr[i-1]+arr[i])

print(prefix_sum_arr)


l_r_arr = [[2,5], [3,4], [1, 4], [5, 7], [0, 5]]

for item in l_r_arr:
    i, j = item
    if i > 0:
        sum_i_j = prefix_sum_arr[j] - prefix_sum_arr[i-1]
        print(sum_i_j)
    else:
        print(prefix_sum_arr[j])


# prefix max

prefix_max = [arr[0]]

for i in range(1, len(arr)):
    prefix_max.append(max(prefix_max[i-1], arr[i]))

print(prefix_max)

# suffix max
n = len(arr)
suffix_max = [0]*n
suffix_max[n-1] = arr[n-1]


for i in range(n-2, -1, -1):
    suffix_max[i] = max(suffix_max[i+1], arr[i])

print(suffix_max)

