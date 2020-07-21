# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18
    if from_index > 0:
        from_index -= 1
    from_index %= 60
    to_index %= 60
    a, b = 0, 1
    sum_upto_m_ = 0
    sum_upto_n_ = 0
    for i in range(from_index):
        a, b = b, (a + b)
        sum_upto_m_ += a
    a, b = 0, 1
    for i in range(to_index):
        a, b = b, (a + b)
        sum_upto_n_ += a
    return sum_upto_n_ % 10 - sum_upto_m_ % 10


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to) % 10)
