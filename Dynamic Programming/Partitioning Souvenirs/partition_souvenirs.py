# python3

from itertools import product
from sys import stdin


def partition3(values):
    assert 1 <= len(values) <= 20
    # assert all(1 <= v <= 30 for v in values)

    s = sum(values)
    if s % 3 == 0:
        capacity = s // 3
        d = [[0 for i in range(capacity + 1)] for j in range(input_n)]
        for i in range(input_n):
            for j in range(capacity + 1):
                if i == 0 and values[i] <= j:
                    d[i][j] = values[i]
                else:
                    if values[i] <= j:
                        v = values[i] + d[i - 1][abs(values[i] - j)]
                        d[i][j] = max(d[i - 1][j], v)
                    else:
                        d[i][j] = d[i - 1][j]
        return 1 if d[input_n-1][capacity] == capacity else 0
    else:
        return 0


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
