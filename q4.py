# Task 1
if not isinstance(s, str):
        print("Error: Input 's' must be a string.")
        return None

    reversed_s = s[::-1]
    return reversed_s
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
