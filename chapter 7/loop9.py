#print multiplication table of a given number using for loop
num=int(input("enter a number"))
for i in range(1,11):
    #so here we  can print the number through two methods from f string and 
 
#     6 X 1=6  
# 6 X 2=12
# 6 X 3=18
# 6 X 4=24
# 6 X 5=30
# 6 X 6=36
# 6 X 7=42
# 6 X 8=48
# 6 X 9=54
# 6 X 10=60
#this is the output
#and now we will learn about second method
 print(f"{num}X{i}={num*i}")