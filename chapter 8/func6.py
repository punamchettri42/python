#solving problems
#python program to find the greatest of three numbers using recursion
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the Third number: "))   #here we have to use int because without the use of int the number is in string form
def find_Biggest():      #function definition
     if(num1>=num2) and (num1>=num2):
         largest=num1
     elif(num2>=num1) and (num2>=num3):
         largest=num2
     else:
         largest=num3
     print("Largest number is",largest)
find_Biggest()      #function call