Bubble Sort

Description

This project contains a Python script that implements the Bubble Sort algorithm to arrange employee salaries in ascending order. Bubble Sort repeatedly compares adjacent elements and swaps them when they are in the wrong order.

Algorithm

The script uses a bubble_sort(arr) function to sort the employee salaries. The step-by-step algorithm is as follows:

Initialize List: Store the employee salaries in an unsorted list.

Start Pass: Begin the first pass through the list and compare adjacent salary values.

Compare Elements: Compare the current element with the next element.

Swap Elements: If the current salary is greater than the next salary, swap their positions.

Repeat Comparisons: Continue comparing adjacent elements until reaching the end of the unsorted portion of the list.

Repeat Passes: Repeat the process for multiple passes. After each pass, the largest unsorted salary moves to its correct position at the end of the list.

Check Swaps: If no elements are swapped during a complete pass, the list is already sorted and the algorithm stops early.

Return Result: Return the sorted list of employee salaries.

Input and Output

Input

Original salaries: [45000, 32000, 58000, 41000, 67000, 38000]

Output

Sorted salaries: [32000, 38000, 41000, 45000, 58000, 67000]
