import math


def swap(values, a, b):

    temp = values[a]
    values[a] = values[b]
    values[b] = temp

def sort(values):

    if len(values) < 2:
        return values

    left = sort(values[:math.floor(len(values)/2)])
    right = sort(values[math.floor(len(values)/2):])

    main_idx = 0
    left_idx = 0
    right_idx = 0

    for i in range(len(values)):
        if left[left_idx] <= right[right_idx]:
            values[i] = left[left_idx]
            left_idx += 1
        else:
            values[i] = right[right_idx]
            right_idx += 1
        main_idx += 1
        if right_idx == len(right) or left_idx == len(left):
            break

    while left_idx < len(left):
        values[main_idx] = left[left_idx]
        left_idx += 1
        main_idx += 1

    while right_idx < len(right):
        values[main_idx] = right[right_idx]
        right_idx += 1
        main_idx += 1

    return values

values = [9, 2, 4, 0, 3, 6, 7, 1, 5, 8]

result = sort(values)
print(result)