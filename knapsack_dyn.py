def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
knapsack_capacity = 50

max_total_value = knapsack_01(weights, values, knapsack_capacity)
print("Maximum total value:", max_total_value)
