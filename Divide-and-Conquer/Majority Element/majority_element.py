# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(n, elements):
    assert n <= 10 ** 5
    dic = {}
    for element in elements:
        dic[element] = dic.get(element, 0) + 1
        if dic[element] > n/2:
            return 1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_n, input_elements))
