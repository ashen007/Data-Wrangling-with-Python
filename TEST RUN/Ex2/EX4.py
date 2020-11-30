def read_data(path):
    with open(path, 'r') as file:
        data = file.read()

    return data


def clean_data(file):
    dataset = read_data(file)
    dataset = dataset.split('\n')
    header = dataset[0].split(',')
    dataset.pop(0)
    dataset.pop()

    for element in dataset:
        row = element.split(',')
        dataset[dataset.index(element)] = row

    for row in dataset:
        row[7] = float(row[7])
        row[8] = float(row[8])
        row[9] = float(row[9])

    return dataset, header
