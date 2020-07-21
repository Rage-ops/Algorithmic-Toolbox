# python3


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18
    a, b = 0, 1
    s = 0
    for i in range(n):
        a, b = b, a+b
        s += a
    return s % 10


if __name__ == '__main__':

    input_n = int(input())
    piscano_period_of_10 = 60
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n % piscano_period_of_10))
