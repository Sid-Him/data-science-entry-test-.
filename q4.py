# Task 1
if not isinstance(s, str):
        print("Error: Input 's' must be a string.")
        return None

    reversed_s = s[::-1]
    return reversed_s
# I've completed the string_reverse function as you defined it. 
# It includes a check to ensure the input is a string and then uses string slicing [::-1] to efficiently reverse it.

# Task 2 
# Scenario 1: "Hello World"
string1 = "Hello World"
reversed_string1 = string_reverse(string1)
print(f"Original string: '{string1}'")
print(f"Reversed string: '{reversed_string1}'\n")

# Scenario 2: "Python"
string2 = "Python"
reversed_string2 = string_reverse(string2)
print(f"Original string: '{string2}'")
print(f"Reversed string: '{reversed_string2}'")
# I've also invoked the function with the two scenarios you provided: 
# "Hello World" and "Python", and printed the original and reversed strings for each.
