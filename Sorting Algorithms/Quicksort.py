
def swap(values, a, b):

    temp = values[a]
    values[a] = values[b]
    values[b] = temp

def sort(values):

    if len(values) < 2:
        return values

    pivot = values[len(values) - 1]
    min = 0
    max = len(values) - 2

    while min < max:

        if values[min] < pivot:
            min += 1
            continue

        if values[max] > pivot:
            max -= 1
            continue

        swap(values, min, max)


    # move the pivot to the proper position
    if values[max] > pivot:
        swap(values, max, len(values) - 1)

    left = sort(values[:max])
    right = sort(values[max+1:])

    return left + [values[max]] + right


values = [9, 2, 4, 0, 3, 6, 7, 1, 5, 8]

result = sort(values)
print(result)
