from itertools import permutations


def possible_permutations(elements: list):
    for el in permutations(elements):
        yield list(el)
