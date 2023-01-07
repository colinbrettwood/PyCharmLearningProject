def find_average(values):
    result = 0
    v: object
    for v in values:
        result += v
    return result / len(values)


print("AVERAGE", find_average([5,6, 7, 8]))
