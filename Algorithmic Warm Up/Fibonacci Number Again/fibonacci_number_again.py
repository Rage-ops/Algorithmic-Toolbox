# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def period_length(m):
    l = []
    a, b = 0, 1
    for i in range(m*m):
        l.append(a)
        a, b = b, (a + b) % m
        if a == 0 and b == 1:
            return i+1, l


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    period, fib_mod_m = period_length(m)
    return fib_mod_m[n % period]




if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
