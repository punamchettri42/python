#python program to read the text from a given file poems.txt and find out whether it contains the word "twinkle"
#first create the txt file named .txt where we can write the poem and then open in th .py mode
f = open('poem.txt')
t = f.read()
if 'twinkle' in t:
    print("twinkle is present")
else:
    print("twinkle is not present")
f.close()