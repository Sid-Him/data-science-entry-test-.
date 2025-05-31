# Task 1 
 if not isinstance(lst, list):
        print("Error: Input 'lst' must be a list.")
        return "Invalid input"

    index = 0
    while index < len(lst):
        current_element = lst[index]
        if isinstance(current_element, (int, float)) and current_element < 0:
            return current_element
        index += 1

    return "No negatives"

# I've implemented the find_first_negative function using a while loop as requested.
# Function Logic (find_first_negative):
# Input Validation: It first checks if the input lst is actually a list. If not, it prints an error and returns "Invalid input".
# Initialization: It initializes an index variable to 0.
# While Loop: The while loop continues as long as index is less than the length of the list.
# Element Check: Inside the loop, it retrieves the current_element at the index. It then checks two conditions:
# Is current_element an instance of int or float (to ensure it's a number)?
# Is current_element less than 0 (i.e., negative)?
# Return First Negative: If both conditions are true, it immediately returns current_element as it's the first negative number found.
# Increment Index: If no negative number is found at the current index, the index is incremented to move to the next element.
# No Negatives Found: If the while loop completes without returning (meaning no negative numbers were found in the entire list), the function returns the string "No negatives".

# Task 2
# Scenario 1: [3, 5, -1, 7, -2, 8]
list1 = [3, 5, -1, 7, -2, 8]
result1 = find_first_negative(list1)
print(f"List: {list1}, First negative: {result1}")
# # In scenario 1, the the expected output is -1

# Scenario 2: [2, 10, 7, 0]
list2 = [2, 10, 7, 0]
result2 = find_first_negative(list2)
print(f"List: {list2}, First negative: {result2}")
# In Scenario 2 the expected output is none.

