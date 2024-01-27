# cook your dish here
n = int(input())
arr = list(map(int, input().split(' ')))

current_minimum = arr[0]
difference_arr = [0]*n

for i in range(1, n):
    if arr[i] < current_minimum:
        current_minimum = arr[i]
    difference_arr[i] = arr[i] - current_minimum

if max(difference_arr) > 0:
    print(max(difference_arr))
else:
    print(0)