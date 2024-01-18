array = [1, 3, 5, 2, 7, 90, 45]

# deep copy - pass by value
arr2 = array.copy()

print(arr2)

array.append(67)

array[1] = 0

print(arr2)

# shallow copy

array3 = array

print(array3)
array[2] = 1

print(array3)