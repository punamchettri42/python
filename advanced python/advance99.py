
list1=[3,53,2,False,6.2,"punam"]
'''
index=0
for item in list1:
    print(item,index)
    index+=1

'''
for index,item in enumerate(list1):
    print(item,index)

    '''
    the global keyword
    global keyword is used to modify the variable outside of the current scope.

    enumerate function in python 
    ___the enumerate function adds counter to an iterable and returns it 

    for i,item in list1:
        print(i,item)
        prints the items of list1 and index
    
    ''' 

    '''
    list comprehensions is an elegant way to create lists based on existing lists.

    lilst1 =[1,7,12,11,22]
    list2=[i for item in list1 if item>8]
    
    
    '''