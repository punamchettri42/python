#there is some other method for doing the file5 in python

content =""
with open("log.txt") as f:
    while content:
        content=f.readline()
        print(content)

        if 'python ' in content.lower():
            print("yes python is present")
        else:
            print("no python is not present")