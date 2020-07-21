# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions

def merge(b: list, c: list, len1, len2):
    global inversions
    p, q = len1, len2
    d, i , j = [], 0, 0
    while i < p and j < q:
        if b[i] <= c[j]:
            d.append(b[i])
            i += 1
        elif c[j] < b[i]:
            d.append(c[j])
            inversions += p - i
            j += 1
    if i < p and j >= q:
        d += b[i:]
    elif j < q and i >= p:
        d += c[j:]
    return d

def mergesort(arr: list, low: int, high: int, n : int):
    if n == 1:
        return [arr[low]]
    mid = (low + high)// 2
    b = mergesort(arr, low, mid, (mid - low) + 1)
    c = mergesort(arr, mid+1, high, high - mid)
    d = merge(b, c, (mid-low) + 1, high - mid)
    return d

def compute_inversions(a, n):
    mergesort(elements, 0, n-1, n)
    return inversions


if __name__ == '__main__':
    inversions = 0
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements, input_n))
