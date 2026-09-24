# Experiment 2 – 0/1 Knapsack

## Aim

Implement Dynamic Programming for the **0/1 Knapsack problem** and analyze its time and space complexity.

## Algorithm / Procedure

1. Take item weights, values, and knapsack capacity.
2. Create a DP table.
3. For every item, decide whether to include or exclude it.
4. Store the maximum value for each capacity.
5. Return the maximum value obtained.

## Program

```python
def knapsack(weights, values, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Input data
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

# Calculate maximum value
print("Maximum value:", knapsack(weights, values, capacity))
```

## Data & Result

### Input

```text
Weights = [2, 3, 4, 5]
Values = [3, 4, 5, 6]
Capacity = 5
```

### Output

```text
Maximum value: 7
```

## Inference & Analysis

Dynamic Programming avoids solving the same subproblems repeatedly by storing the results in a DP table.

* **Time Complexity:** O(nW)
* **Space Complexity:** O(nW)

Where:

* `n` = number of items
* `W` = knapsack capacity

## Result

Thus, the **0/1 Knapsack problem was successfully implemented using Dynamic Programming**, and its time and space complexities were analyzed.
