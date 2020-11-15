def swap(values, a, b):
    temp = values[a]
    values[a] = values[b]
    values[b] = temp


def sort(values):
    if len(values) < 2:
        return values

    for i in range(1, len(values)):
        for j in range(i, 0, -1):
            if values[j] < values[j - 1]:
                swap(values, j, j - 1)
            else:
                break

    return values


values = [9, 2, 4, 0, 3, 6, 7, 1, 5, 8]

result = sort(values)
print(result)
