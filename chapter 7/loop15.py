#python program to print the multiplication table of for loop  in reverse order
table = int(input("Enter the table: "))

limit = int(input("Enter the ending : "))

for i in range(limit,0,-1):
    print(i,"*",table,"=",i*table)
    #so the output in the given python program is when i keep number 7 and ending 10
#     10 * 7 = 70
# 9 * 7 = 63 
# 8 * 7 = 56 
# 7 * 7 = 49 
# 6 * 7 = 42 
# 5 * 7 = 35 
# 4 * 7 = 28 
# 3 * 7 = 21
# 2 * 7 = 14
# 1 * 7 = 7