#python program to detect spam
text =input("enter the text")
if("make a lot of money"):
    spam =True           #here in python space is very immportant to understand where to keep and wwhere not to

elif("buy now " in text):
        spam= True
elif("click this" in text):
    spam =True
elif("subscribe this " in text):
    spam =True
else:
        spam=False

if(spam):
     print("this text is spam")
else:
    print("this text is not spam")

         
