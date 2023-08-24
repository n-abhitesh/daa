def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    fractions_taken = [0] * len(items)

    for i, (weight, value) in enumerate(items):
        if capacity == 0:
            break
        fraction = min(1, capacity / weight)
        total_value += fraction * value
        fractions_taken[i] = fraction
        capacity -= fraction * weight

    return total_value, fractions_taken

# Example usage
items = [(10, 60), (20, 100), (30, 120)]
knapsack_capacity = 50

total_value, fractions_taken = fractional_knapsack(items, knapsack_capacity)

print("Maximum total value:", total_value)
print("Fractions taken for each item:")
for i, fraction in enumerate(fractions_taken):
    print(f"Item {i+1}: {fraction:.2f}")
