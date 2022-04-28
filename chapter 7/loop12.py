# Write a program to find the sum of first n natural numbers using a while loop.
#python program to find the sum of first n natural numbers using a while loop
n = input("Enter Number to calculate sum")
n = int (n)
sum = 0
for num in range(0, n+1, 1):
    sum = sum+num
print("SUM of first ", n, "numbers is: ", sum )