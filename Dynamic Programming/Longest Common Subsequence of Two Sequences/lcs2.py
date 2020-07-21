# python3


def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    d = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                d[i][j] = 0
            elif first_sequence[i-1] == second_sequence[j-1]:
                d[i][j] = d[i-1][j-1] + 1
            else:
                d[i][j] = max(d[i-1][j], d[i][j-1])
    # print(d)
    return d[n][m]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
