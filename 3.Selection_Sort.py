def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i   # assume the first element is minimum
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # update index of minimum element
        # Swap the found minimum with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selectionSort([89, 56, 45, 34, 65, 76]))
