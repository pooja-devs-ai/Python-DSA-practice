"""
💡 Problem Statement:
Given a sorted list of integers and a target number,
write a function that returns True if the target exists in the list,
otherwise returns False. Use Binary Search logic.
"""

def check_presence(arr, target):
    low = 0                              # Starting index of the list
    high = len(arr) - 1                  # Ending index of the list

    while low <= high:
        mid = (low + high) // 2          # Middle index of the current search space

        if arr[mid] == target:           # If target found at mid
            return True
        elif arr[mid] < target:          # If target is in the right half
            low = mid + 1
        else:                            # If target is in the left half
            high = mid - 1

    return False                         # Target not found in the list

# 🚀 Taking input from the user
n = int(input("Enter the length of the list: "))
nums = []

for i in range(n):
    element = int(input("Enter the element: "))
    nums.append(element)

sorted_array = sorted(nums)              # Sorting the list before applying binary search
target = int(input("Enter the number to search in the list: "))

# 🧪 Running the check_presence() function
result = check_presence(sorted_array, target)

if result:
    print(f"The element {target} is present in the list.")
else:
    print(f"The element {target} is not present in the list.")