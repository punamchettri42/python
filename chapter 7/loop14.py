        #        *
        #     *  *  *
        #  *  *  *  *  *
        #okay print the following pattern using python
#  This is the example of print simple reversed right angle pyramid pattern  
rows = int(input("Enter the number of rows:"))  
k = 2 * rows - 2  # It is used for number of spaces  
for i in range(0, rows):  
    for j in range(0, k):  
        print(end=" ")  
    k = k - 2   # decrement k value after each iteration  
    for j in range(0, i + 1):  
        print("* ", end="")  # printing star  
    print("")  

    #so here i came to conclusion that i hate pattern programming in python it is such a mess to learn