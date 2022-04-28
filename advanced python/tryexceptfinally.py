try:
    i=int(input("enter a numebr"))
    c=1/i
except Exception as e:  #here e must be in capital else it will throw an error in python we should be somuch careful about where to keep space where not and many things
    print(e)
finally:
    print("we are done")
