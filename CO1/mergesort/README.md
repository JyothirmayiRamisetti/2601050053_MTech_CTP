Merge Sort

Description

This project contains a Python script that implements the Merge Sort algorithm to arrange a list of student marks in ascending order. The algorithm uses the divide-and-conquer technique by repeatedly dividing the list into smaller parts and then merging the sorted parts.

Algorithm

The script uses a merge_sort(arr) function to sort the marks efficiently. The step-by-step algorithm is as follows:

Check List: If the list contains zero or one element, return the list because it is already sorted.

Divide the List: Find the middle position of the list and divide it into two parts, left and right.

Sort Left Half: Recursively apply Merge Sort to the left half of the list.

Sort Right Half: Recursively apply Merge Sort to the right half of the list.

Merge: Compare the elements from the sorted left and right halves and place the smaller element into the result list.

Add Remaining Elements: After one half is completely processed, add the remaining elements from the other half to the result.

Return Result: Return the completely sorted list.

Input and Output

Input

Original marks: [78, 91, 68, 95, 84, 73, 88, 62]

Output

Sorted marks: [62, 68, 73, 78, 84, 88, 91, 95]
