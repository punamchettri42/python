#file input output
#the ranndom acess memory is volatile and all its contents are last once a program terminates in order to persist the data forever we use files a file is data stored in a storage devicef  A python program can talk to the file by reading content from it and writting content  to it

# types of files 
'''
            text files (.txt,.c etc)
           binary files (.jpg ,.dat etc)

        

'''
#python has a lot of functions for reading updating and deleting files
'''
  opening a file 
  python has an open() function for opening the files.it takes two parameters filename and mode
  for opening 
  open("this.txt","r")
  where this.txt is filename and r is read mode and also open is built in function
  f=open(" this.txt","w")
  f.write("this is nice")
  f.close()
'''
#with statement
'''
 with open("this.txt") as f 
 f.read()
'''
#here no necessary to write f.close as it is done automatically
''' 
so for reading a file in python f=open("this.txt","r")
text =f.read()
print(text)
f.close()
'''

#we can also specify the number of  characters in read() function f.read(2)


#other methods to read the file  we can also use f.readline() function to read on full line at a time
'''
r  equals open for reading 
w equals open for writting 
a equals open for appending 
plus equals for updating
and rb equals reading in binary mode 
and rt equals reading in text mode 
writting files in python 
in order to write a fiel we first open it in write or append mode after which we use the pythons f.write() method to write a file

'''

''''
 we use f.write() to write a file in python
'''