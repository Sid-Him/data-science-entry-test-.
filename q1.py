def swap_values(x, y):
# Task 1
    # Check if both x and y are numeric
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1

    # Swap using only x and y
    x = x + y
    y = x - y
    x = x - y

    print("Swapped values:")
    print("x =", x)
    print("y =", y)
    return 0  # Indicate success
    
# Task 2
# Scenario 1: Non-numeric input
result1 = swap_values("Apple", 10)
print("Result 1:", result1)  # Should return -1

# Scenario 2: Both numeric
result2 = swap_values(9, 17)
print("Result 2:", result2)  # Should print swapped values and return 0
