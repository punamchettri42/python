try:
    i=int(input("enter a number"))
    c=1/i
except Exception as e:
    print(e)
else:
    print("we were sucessful")
    
    '''
    here try with finally _python opens a finally clause which ensures execution of a piece of code irrespective of the exception
    try:
        #some code
    except:
        #some code
    finally:
        #some code
    '''