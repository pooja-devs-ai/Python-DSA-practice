#🧩 1. 2D Array Traversal (Row-wise and column-wise)

#Problem: Write a program to take a 2D list and print all elements row-wise and column-wise.

# we'll write a function named print_elements to traverse an array as functions are reusable and help organize code efficiently
def print_elements(matrix):
    rows=len(matrix)
    columns=len(matrix[0])
    #to print row-wise elements
    print("Row-wise elements:")
    for i in range(rows):         #row-initialisation
        for j in range(columns):  #column-initialisation
            print(matrix[i][j],end=' ')  
    print()                                #new line to separate outputs
    #to print column-wise elements
    print("Column-wise elements:")
    for j in range(columns):          #column-initialisation
        for i in range(rows):         #row-initialisation
            print(matrix[i][j],end=' ')

array=[                              #input matrix
    [2,6,8],
    [5,7,9],
    [2,6,3]
]
print_elements(array)             #function call

