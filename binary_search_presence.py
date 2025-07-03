#💡 Problem Statement:

#Given a sorted list of integers and a target number,
        #write a function that returns True if the target exists in the list,otherwise returns False. Use Binary Search logic.

#function named check_presence will be used to check the presence of the target using binary search

def check_presence(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return True
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
            
        
    return False

n=int(input("Enter the length of the list:"))
nums=[]
for i in range(n):
    element=int(input("Enter the element:"))
    nums.append(element)

sorted_array=sorted(nums)
target=int(input("enter the number to search in the list:"))
result=check_presence(sorted_array,target)
if result==True:
    print(f"The element {target} is present in the list")
else:
    print(f"The element {target} is not present in the list")