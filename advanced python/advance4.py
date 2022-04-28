'''
some code format for exceptional case

#code

except zeroDivisionError:
    #code
except TypeError:
    #code
except:
    #code


'''


''''

raising exceptions 
we can raise exception using the raise keyword in python

'''
def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("this is not good harry")

a=increment('df364')
print(a)