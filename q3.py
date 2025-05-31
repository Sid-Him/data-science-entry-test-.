# Task 1
 # Check if the key already exists in the dictionary
    if key in dct:
        # If the key exists, print its original value
        print(f"Key '{key}' already exists. Original value: {dct[key]}")
    
    # Update the dictionary with the new key-value pair (or update existing key)
    dct[key] = value
    
    # Return the updated dictionary
    return dct
# I've completed the update_dictionary function as per your requirements.
# Function Logic (update_dictionary):
# It checks if the key already exists in the dct using the in operator.
# If the key exists, it prints the original value associated with that key.
# Regardless of whether the key existed or not, it then updates the dictionary with the new key-value pair (dct[key] = value). 
# If the key was new, it's added; if it existed, its value is overwritten.
# Finally, it returns the modified dictionary.

# Task 2
Scenario 1: {}, "name", "Alice"
initial_dict1 = {}
new_key1 = "name"
new_value1 = "Alice"
print(f"Scenario 1: Initial dictionary: {initial_dict1}")
updated_dict1 = update_dictionary(initial_dict1, new_key1, new_value1)
print(f"Updated dictionary: {updated_dict1}\n")

# Scenario 2: {"age": 25}, "age", 26
initial_dict2 = {"age": 25}
new_key2 = "age"
new_value2 = 26
print(f"Scenario 2: Initial dictionary: {initial_dict2}")
updated_dict2 = update_dictionary(initial_dict2, new_key2, new_value2)
print(f"Updated dictionary: {updated_dict2}")
# I then invoked the function with the two specified scenarios, printing the initial and updated dictionaries for each to clearly show the changes.
