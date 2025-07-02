#🧩 3. Print Elements Greater Than the Average.
#Problem Statement:
#Given a list of numbers:

               #Calculate the average of the list
               #Print all elements that are greater than the average

# using a function called print_greater_than_average(arr) to find the elements that satisfy the condition

def print_greater_than_average(arr):
    average=sum(arr)/len(arr)             #to claculate the average,the in-built function sum can be used
    nums_greater_than_average=[]          #empty list to store the elements that satisfy the condition
    for i in range(len(arr)):
        if arr[i]>average:                 #condition that selects the elements to store in the empty list
            nums_greater_than_average.append(arr[i])        #adding the element to the list
    return nums_greater_than_average        #returning the list containing the elements which satisfy the condition

n=int(input("Enter the length of the list: "))   #length input from the user
nums=[]                                     # and empty list to store the elements entered by user
for i in range(n):                            # to take input from the user
    num=int(input("Enter the element: "))
    nums.append(num) 
result=print_greater_than_average(nums)   #function call
print('Numbers greater than average of the list are: ',result)