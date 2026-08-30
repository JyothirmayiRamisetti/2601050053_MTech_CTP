
Maximum Subarray

Description

This project contains a Python script that implements the Maximum Subarray algorithm using Kadane's Algorithm. The project analyzes a list of daily profit and loss values and finds the continuous period that produces the maximum total profit.

Algorithm

The script uses a maximum_subarray(arr) function to find the maximum sum efficiently. The step-by-step algorithm is as follows:

Initialize Values: Set current_sum and max_sum to the first element of the list.

Iterate: Start from the second element and process each value in the list.

Check New Subarray: Compare the current value with the sum of the current subarray plus the current value.

Start New Subarray: If the current value is greater, start a new subarray from the current position.

Extend Subarray: Otherwise, add the current value to the existing subarray.

Update Maximum: If the current sum is greater than the maximum sum found so far, update max_sum and store the starting and ending positions.

Return Result: After processing all values, return the maximum sum and the start and end positions of the maximum subarray.

Input and Output

Input

Daily profit/loss: [10, -3, 5, -8, 12, 7, -2, 4, -15, 8]

Output

Maximum profit: 33
Best period starts at day: 1
Best period ends at day: 8
Best period values: [10, -3, 5, -8, 12, 7, -2, 4]
