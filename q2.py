# Task 1
if not isinstance(lst, list):
        print("Error: Input 'lst' must be a list.")
        return lst  # Return the original list if it's not a list

    modified_list = [replace_val if item == find_val else item for item in lst]
    return modified_list
# I've completed the find_and_replace function. 
# It first checks if the input lst is indeed a list. 
# If not, it prints an error message and returns the original (unmodified) list. 
# If it is a list, it uses a list comprehension to create a new list where all occurrences of find_val are replaced with replace_val, leaving other elements unchanged. 
# Finally, it returns this modified list.

# Task 2
# Scenario 1: [1, 2, 3, 4, 2, 2], 2, 5
list1 = [1, 2, 3, 4, 2, 2]
find_value1 = 2
replace_value1 = 5
modified_list1 = find_and_replace(list1, find_value1, replace_value1)
print(f"Original list: {list1}, Find: {find_value1}, Replace: {replace_value1}")
print(f"Modified list: {modified_list1}\n")

# Scenario 2: ["apple", "banana", "apple"], "apple", "orange"
list2 = ["apple", "banana", "apple"]
find_value2 = "apple"
replace_value2 = "orange"
modified_list2 = find_and_replace(list2, find_value2, replace_value2)
print(f"Original list: {list2}, Find: '{find_value2}', Replace: '{replace_value2}'")
print(f"Modified list: {modified_list2}")

# Then, I invoked the function with the two scenarios you provided, printing both the original and the modified lists for clarity.
