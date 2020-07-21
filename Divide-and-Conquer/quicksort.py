def partition(arr, low, high):
    pivot = arr[low]
    i, j = low+1, high
    while i <= j:
        while i <= high and arr[i] <= pivot:
            i += 1
        while j >= low and arr[j] > pivot :
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    arr[low], arr[i-1] = arr[i-1], arr[low]
    return i-1


def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr,low, p-1)
        quicksort(arr, p+1, high)


arr = [int(x) for x in input().split()]
quicksort(arr,0,len(arr)-1)
print(arr)