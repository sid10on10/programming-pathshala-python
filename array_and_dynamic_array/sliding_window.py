






# minimum swaps to get contigous sub array of elements less than or equal to k
n, k = list(map(int, input().split(' ')))
arr = list(map(int, input().split(' ')))

c_l_e = len(list(filter(lambda x:x<=k, arr)))

maximum = float('-inf')
starting_count = len(list(filter(lambda x:x<=k, arr[:c_l_e])))
legal_e_arr = [starting_count] 
current_count = starting_count
for j in range(c_l_e, n):
    if arr[j] <= k:
        current_count += 1
    if arr[j-c_l_e] <= k:
        current_count -= 1
    legal_e_arr.append(current_count)

print(c_l_e-max(legal_e_arr))
        
    
    
    
    