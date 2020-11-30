import itertools
import random


def test():
    rand_num = [random.randint(0, 25) for i in range(10)]
    per_num = []
    dropped = []

    permute = itertools.permutations(range(10), 2)
    drop = itertools.dropwhile(lambda x: x % 4 == 0, rand_num)

    for number in permute:
        per_num.append(number)

    for number in drop:
        dropped.append(number)

    print(rand_num, per_num, dropped, sep='\n')

