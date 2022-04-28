'''
file contains a word donkey multiple times you need to write a program which replaaces this word ##### by updating the same
file
'''

with open("sample.txt") as f:
    content =f.read()

content=content.replace("donkey","@#$%^&")

with open("sample.txt","w") as f:
    content =f.write(content)