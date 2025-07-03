#🧩 Mega Challenge — List Filtering, Frequency & Indexing
#💡 Problem Statement:

#Write a Python program that does the following tasks on a list of integers:

                    #Find the index of the first number that appears only once in the list

                    #Print all numbers that appear more than once, along with their frequencies

                    #Print only the elements at even indices (0, 2, 4, …)

def advanced_list_analysis(List):
    more_than_once={}                                    #to store the elements with their respective frequencies
    elements_at_even_indices=[List[i] for i in range(0,len(List),2)]     #elements at even indices evaluated using list comprehension
    first_non_repeated_element=0                          #to store the first non repeated element
    first_non_repeated_element_index=-1                 #first non repeated element's index in the variable first_non_repeated_element_index
    
    for i in range(len(List)):
        
        if List.count(List[i])==1:                         #to check non-repeatence of the element using count()method
            first_non_repeated_element=List[i]
            first_non_repeated_element_index=i
            break                                         #once the fisrt non repeated element is encountered,the loop should break
        
    for item in List:
        if item not in more_than_once:
            more_than_once[item]=1                        #initialising the key-value pair if the key is not present
        
        else:
            more_than_once[item]+=1                       #incrementing the value count if key already exists

    return first_non_repeated_element,first_non_repeated_element_index,more_than_once,elements_at_even_indices      #returning the outputs

Lst=[4, 5, 2, 4, 3, 5, 9]
result=advanced_list_analysis(Lst)

print(f"First non-repeated element is {result[0]} at index {result[1]}.")    #to print the first non repeated element and its index

print("Repeated elements with frequencies:")

for keys,values in result[2].items():
    if values>1:                                      #to check the key has occurred more than once and then print only those items
        print(f"{keys}-->{values}")                   #to print the repeated  element and its frequency of occurrence

print(f"Elements at even indices :{result[3]}")            #to print the elements at even indices

