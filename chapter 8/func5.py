#programmers should be very sure and extremely careful while working on function and recursion
#recursion is the easiest method to solve the problem it is also  the direct method of solving the problem
def factorial(n):
    
if i == 0 or i == 1 : #Base condition which doesn’t call the function any further
	return i
	else:
		return n*factorial(n-1) #Function calling itself
