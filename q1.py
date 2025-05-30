def swap_values(x, y):
    # Check if both x and y are numeric (int or float)
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1

    # Swapping using arithmetic operations without a third variable
    x = x + y
    y = x - y
    x = x - y

    # Print the swapped values
    print(f"Swapped values: x = {x}, y = {y}")
