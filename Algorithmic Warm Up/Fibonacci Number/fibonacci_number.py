# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n, l):
    assert 0 <= n <= 45
    if n <= 1:
        return l[n]
    else:
        try:
            return l[n]
        except KeyError:
            l[n] = fibonacci_number(n - 1, l) + fibonacci_number(n - 2, l)
            return l[n]

def fib(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

if __name__ == '__main__':
    input_n = int(input())
    #print(fibonacci_number(input_n, {0: 0, 1: 1}))
    print(fib(input_n))
