def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[1])  # Sort jobs by finish time
    n = len(jobs)
    max_profit = [0] * n
    max_profit[0] = jobs[0][2]

    for i in range(1, n):
        # Find the latest non-overlapping job
        j = i - 1
        while j >= 0 and jobs[j][1] > jobs[i][0]:
            j -= 1

        # Consider including the current job or excluding it
        max_profit[i] = max(max_profit[i - 1], jobs[i][2] + (max_profit[j] if j >= 0 else 0))

    return max_profit[n - 1]

# Example usage
jobs = [(1, 4, 20), (2, 5, 10), (3, 6, 30), (5, 7, 25), (6, 8, 15), (7, 9, 5)]

max_total_profit = job_scheduling(jobs)
print("Maximum total profit:", max_total_profit)
