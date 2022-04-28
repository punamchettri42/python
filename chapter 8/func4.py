def factorial_iter(n):
    product =1
    for i in range(n):
        product = product*(i+1)
    return product      #here in this code we can find about recursionS recursion helps to solve the problem easily
def factorial_recursive(n):
    if n ==1 or n==0:
        return 1 
    return n *factorial_recursive(n-1)   #here this is recursion

# f= factorial_iter(5)
f=factorial_recursive(0)
print(f)