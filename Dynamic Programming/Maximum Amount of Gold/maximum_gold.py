# python3

from sys import stdin


def maximum_gold(capacity, weights):

    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    d = [[0 for i in range(capacity+1)] for j in range(n)]
    for i in range(n):
        for j in range(input_capacity+1):
            if i == 0 and weights[i] <= j:
                d[i][j] = values[i]
            else:
                # Considering the bar
                if weights[i] <= j:
                    v = values[i] + d[i-1][abs(weights[i] - j)]
                    d[i][j] = max(d[i-1][j], v)
                else:
                    d[i][j] = d[i-1][j]

    print(d)
    return d[n-1][input_capacity]

if __name__ == '__main__':
    # input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    # assert len(input_weights) == n
    input_capacity, n = map(int, input().split())
    input_weights = [int(x) for x in input().split()]
    values = input_weights.copy()
    print(maximum_gold(input_capacity, input_weights))
