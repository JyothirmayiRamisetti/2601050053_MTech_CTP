# Experiment 1 — Merge Sort

## Aim

To implement the **Merge Sort algorithm using Divide and Conquer** and calculate its time complexity.

## Algorithm / Procedure

1. Start with an unsorted list of elements.
2. If the list contains one or zero elements, return it because it is already sorted.
3. Find the middle position of the list.
4. Divide the list into two halves.
5. Recursively apply Merge Sort to the left half.
6. Recursively apply Merge Sort to the right half.
7. Merge the two sorted halves.
8. Compare elements from both halves and place the smaller element into the result.
9. Continue until all elements are merged.
10. Display the sorted list.

## Program

```python
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
```

## Sample Input

```text
Enter elements separated by space: 38 27 43 3 9 82 10
```

## Sample Output

```text
Original list: [38, 27, 43, 3, 9, 82, 10]
Sorted list: [3, 9, 10, 27, 38, 43, 82]
```

## Time Complexity

Merge Sort divides the array into two halves recursively.

| Case         | Time Complexity |
| ------------ | --------------- |
| Best Case    | O(n log n)      |
| Average Case | O(n log n)      |
| Worst Case   | O(n log n)      |

**Space Complexity:** O(n)

## Inference & Analysis

The Merge Sort algorithm successfully sorts the given elements using the **Divide-and-Conquer technique**. The array is repeatedly divided into smaller subarrays and then merged in sorted order. Its time complexity is **O(n log n)** for the best, average, and worst cases.

## Result

Thus, the **Merge Sort algorithm was successfully implemented using Divide and Conquer**.

