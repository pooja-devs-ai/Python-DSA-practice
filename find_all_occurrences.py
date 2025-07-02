#🧩 Find All Occurrences of a Target in a List

#writing a function called find_all_occurrences to do the task efficiently and reuse the code

def find_all_occurrences(arr, target):
    occurred_elements=[]  #an empty list to store the indices where the target occurs
    for i in range(len(arr)):  #specifying the loop condition
        if arr[i]==target:        
            occurred_elements.append(i)       #appending the index to the empty element if the number in the arr matches with the target.
    return occurred_elements

n=int(input("Enter the length of the list: "))   #length input from the user
array=[]                                     # and empty list to store the elements entered by user
for i in range(n):                            # to take input from the user
    num=int(input("Enter the element: "))
    array.append(num)                       #to add the element to the empty list

target=int(input("Enter a number to count its occurrences in the list:")) #prompting the user to input the target
result=find_all_occurrences(array,target)        #function call with user inputs
print(result)                                     #printing the result of the task done by the function
