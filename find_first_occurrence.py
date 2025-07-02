def find_first_occurrence(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

arr = [4, 5, 1, 2, 5, 4, 1, 2]
target = 5

result = find_first_occurrence(arr, target)

if result != -1:
    print(f"First occurrence of {target} is at index {result}.")
else:
    print(f"{target} not found in the list.")
