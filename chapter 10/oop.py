'''
here we will be learning object oriented programming

'''


''''
solving a problem by creating objects is one of the most popular approached in programming .this is called object oriented 
programming.

this concept focuses on using reusable code.


CLASS

class is a blueprint for creating objects


'''
# a=12
# b=34
# print("the sum of a and b is ",a+b)

'''
so we will solve this using oop

in oop we use function as well
'''
class number:
    def sum(self):
        return self.a + self.b

num=number()
num.a =12
num.b =34
s=num.sum()
print(s)
