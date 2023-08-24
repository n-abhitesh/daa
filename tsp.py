def tsp(graph):
    n = len(graph)
    all_mask = (1 << n) - 1

    dp = [[float('inf')] * n for _ in range(all_mask + 1)]
    dp[1][0] = 0

    for mask in range(1, all_mask + 1):
        for u in range(n):
            if mask & (1 << u):
                for v in range(n):
                    if v != u and mask & (1 << v):
                        dp[mask][u] = min(dp[mask][u], dp[mask ^ (1 << u)][v] + graph[v][u])

    min_dist = float('inf')
    for v in range(1, n):
        min_dist = min(min_dist, dp[all_mask][v] + graph[v][0])

    return min_dist

# Example usage
graph = [
    [0, 29, 20, 21],
    [29, 0, 15, 18],
    [20, 15, 0, 16],
    [21, 18, 16, 0]
]

min_distance = tsp(graph)
print("Minimum distance for TSP:", min_distance)
