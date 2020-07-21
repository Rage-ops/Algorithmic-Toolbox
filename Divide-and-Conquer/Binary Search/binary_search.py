# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query, n, k):
    # assert all(keys[i] < keys[i + 1] for i in range(n - 1))
    # assert all(1 <= keys[i] <= 10 ** 9 for i in range(n))
    assert 1 <= n <= 3 * 10 ** 4
    assert 1 <= k <= 10 ** 5
    low, high = 0, n-1
    if keys[0] <= query <= keys[-1]:
        while low <= high:
            mid = (low + high)//2
            if keys[mid] == query:
                return mid
            elif keys[mid] < query:
                low = mid + 1
            elif keys[mid] > query:
                high = mid - 1
    return -1

if __name__ == '__main__':
    input_keys = list(map(int, input().split()))
    n, input_keys = input_keys[0], input_keys[1:]
    input_queries = list(map(int, input().split()))
    k, input_queries = input_queries[0], input_queries[1:]
    # assert all(input_queries[j] < 10 ** 9 for j in range(k))
    for q in input_queries:
        print(binary_search(input_keys, q, n, k), end=' ')
