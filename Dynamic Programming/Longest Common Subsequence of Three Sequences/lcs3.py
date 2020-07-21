# python3


def lcs3(first_sequence, second_sequence, third_sequence):
    assert n <= 100
    assert m <= 100
    assert q <= 100

    l = [[[0 for i in range(q+1)] for j in range(m+1)]for k in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            for k in range(q+1):
                if i == 0 or j == 0 or k == 0:
                    l[i][j][k] = 0
                elif first_sequence[i - 1] == second_sequence[j-1] and first_sequence[i-1] == third_sequence[k-1]:
                    l[i][j][k] = l[i-1][j-1][k-1] + 1
                else:
                    l[i][j][k] = max(l[i-1][j][k], l[i][j-1][k], l[i][j][k-1])
    return l[n][m][q]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
