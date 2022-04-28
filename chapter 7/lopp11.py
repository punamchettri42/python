#checking prime or not

num=int(input("enter a number"))

for i in range(2,num):
 if (num%i == 0):
  print("this number is prime")