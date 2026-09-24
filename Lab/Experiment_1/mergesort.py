def merge_sort(arr):
    # Base condition
    if len(arr) <= 1:
        return arr

    # Find middle
    mid = len(arr) // 2

    # Divide
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge
    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Input
arr = list(map(int, input("Enter elements separated by space: ").split()))

print("Original list:", arr)

sorted_arr = merge_sort(arr)

print("Sorted list:", sorted_arr)
