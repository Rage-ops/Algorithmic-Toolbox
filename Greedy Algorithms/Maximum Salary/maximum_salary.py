# python3

from itertools import permutations
from functools import cmp_to_key


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest

def compare(a, b):
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
    if ab > ba:
        return -1
    elif ba > ab:
        return 1
    return 0

def largest_number(numbers):
    ans = sorted(numbers, key=cmp_to_key(compare))
    return ''.join(str(i) for i in ans)


if __name__ == '__main__':
    n = int(input())
    input_numbers = [int(x) for x in input().split()]
    assert len(input_numbers) == n
    print(largest_number(input_numbers))



