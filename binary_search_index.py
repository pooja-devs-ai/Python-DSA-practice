'''💡 Problem Statement:
Given a sorted list of integers and a target number,
write a function that returns the index of the target in the list using Binary Search.

If the target is **not found**, return -1.'''

#writing a function called return_the_index to get the index of the target in the list using binary search

def return_the_index(arr,target):
    low = 0                              # Starting index of the list
    high = len(arr) - 1                  # Ending index of the list

    while low <= high:
        mid = (low + high) // 2          # Middle index of the current search space

        if arr[mid] == target:           # If target found at mid
            return mid
        elif arr[mid] < target:          # If target is in the right half
            low = mid + 1
        else:                            # If target is in the left half
            high = mid - 1

    return -1                            #if target not found in the list

n = int(input("Enter the length of the list: "))
nums = []

for i in range(n):
    element = int(input("Enter the element: "))
    nums.append(element)

sorted_array = sorted(nums)              # Sorting the list before applying binary search
target = int(input("Enter the number to search in the list: "))
print(f'The array sent to the the function is :{sorted_array}')

# 🧪 Running the return_the_index() function
result = return_the_index(sorted_array, target)

if result!=-1:
    print(f"Target {target} found at {result} ")
else:
    print(f"Target {target} not found in the list")