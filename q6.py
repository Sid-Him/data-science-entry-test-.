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
# Task 2
# Scenario 1: [3, 5, -1, 7, -2, 8]
list1 = [3, 5, -1, 7, -2, 8]
result1 = find_first_negative(list1)
print(f"List: {list1}, First negative: {result1}\n")

# Scenario 2: [2, 10, 7, 0]
list2 = [2, 10, 7, 0]
result2 = find_first_negative(list2)
print(f"List: {list2}, First negative: {result2}")
