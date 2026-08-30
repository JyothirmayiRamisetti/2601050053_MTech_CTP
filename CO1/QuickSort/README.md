
Quick Sort

Description

This project contains a Python script that implements the Quick Sort algorithm to arrange a list of product prices in ascending order. Quick Sort uses the divide-and-conquer technique by selecting a pivot element and dividing the list into smaller parts.

Algorithm

The script uses a quick_sort(arr) function to sort the product prices efficiently. The step-by-step algorithm is as follows:

Check List: If the list contains zero or one element, return the list because it is already sorted.

Select Pivot: Choose the middle element of the list as the pivot.

Partition the List: Compare each element with the pivot and divide the elements into three groups.

Left Group: Store all elements smaller than the pivot.

Middle Group: Store all elements equal to the pivot.

Right Group: Store all elements greater than the pivot.

Recursive Sorting: Apply Quick Sort recursively to the left and right groups.

Combine Results: Combine the sorted left group, middle group, and sorted right group to produce the final sorted list.

Input and Output

Input

Original product prices: [850, 450, 12500, 250, 1800, 3200, 1400, 2600]

Output

Sorted product prices: [250, 450, 850, 1400, 1800, 2600, 3200, 12500]
