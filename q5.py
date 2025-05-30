# Task 1
# Check if both num and divisor are numeric
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        print("Error: Both 'num' and 'divisor' must be numeric.")
        return False  # Or raise a TypeError, depending on desired error handling

    # Handle the case where divisor is zero to prevent ZeroDivisionError
    if divisor == 0:
        print("Error: Divisor cannot be zero.")
        return False

    # Check for divisibility using the modulo operator
    # For floating-point numbers, direct modulo might not be exact,
    # so we check if the remainder is very close to zero.
    if isinstance(num, float) or isinstance(divisor, float):
        # Using a small tolerance for float comparisons
        return abs(num % divisor) < 1e-9
    else:
        return num % divisor == 0
# Task 2
# Scenario 1: 10, 2
number1 = 10
div1 = 2
result1 = check_divisibility(number1, div1)
print(f"Is {number1} divisible by {div1}? {result1}\n")

# Scenario 2: 7, 3
number2 = 7
div2 = 3
result2 = check_divisibility(number2, div2)
print(f"Is {number2} divisible by {div2}? {result2}\n")
