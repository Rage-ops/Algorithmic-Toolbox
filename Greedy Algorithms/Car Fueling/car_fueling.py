# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    min_refills, curr_refill = 0, -1
    pos_of_car = 0
    while curr_refill < input_n - 1:
        last_refill = curr_refill
        while curr_refill < input_n-1 and stops[curr_refill + 1] - pos_of_car <= input_m:
            curr_refill += 1
        if curr_refill == last_refill:
            break
        if curr_refill <= input_n - 1 and d - pos_of_car > m:
            min_refills += 1
        pos_of_car = stops[curr_refill]
    if d - pos_of_car > m:
        return -1
    return min_refills


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
