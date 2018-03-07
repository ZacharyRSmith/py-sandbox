def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


def normalize_copy(numbers):
    numbers = list(numbers)
    total = sum(numbers)
    result = []
    for val in numbers:
        percent = 100 * val / total
        result.append(percent)
    return result


def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for val in get_iter():
        percent = 100 * val / total
        result.append(percent)
    return result


# it = read_visits('./my_numbers.txt')
# percentages = normalize_copy(it)
percentages = normalize_func(lambda: read_visits('./my_numbers.txt'))
print(percentages)
