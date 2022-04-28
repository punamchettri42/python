#renaming a file
import os

oldname ="sample2.txt"
newname ="renamed_by_python.txt"
with open(oldname) as f:
    content =f.read()

with open(newname,"w") as f:
    f.write(content)

os.remove(oldname)


'''
so in all i did not kneew a lot about file handling
but i also i will be keep learning and exploring more and more

'''