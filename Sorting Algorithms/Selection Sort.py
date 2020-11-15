
def swap(values, a, b):
    """Swap positions a and b in values"""
    temp = values[a]
    values[a] = values[b]
    values[b] = temp

def sort(values):

    if len(values) < 2:
        return values

    for i in range(0, len(values) - 1):
        smallest = values[i]
        index = i
        for j in range(i + 1, len(values)):
            if values[j] < smallest:
                smallest = values[j]
                index = j

        swap(values, index, i)

    return values


values = [9, 2, 4, 0, 3, 6, 7, 1, 5, 8]

result = sort(values)
print(result)