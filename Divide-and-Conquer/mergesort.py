def merge(b: list, c: list, len1, len2):
    p, q = len1, len2
    d, i , j = [], 0, 0
    while i < p and j < q:
        if b[i] <= c[j]:
            d.append(b[i])
            i += 1
        elif c[j] < b[i]:
            d.append(c[j])
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

    