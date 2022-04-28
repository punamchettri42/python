try:
    a=int(input("enter a number"))
    c=1/a
except Exception  as e:
    print("exception occured")
print(e)