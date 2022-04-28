'''
 python program that lets a user play a game and returns the score as an integer a and read  aa file 'hiscore.txt' which is either black or contains the previous hi_score 
'''
def game():
     return  

score=game()
with open("hiscore.txt") as f:
    hiscore =int(f.read())

if hiscore<score:
    with open("hiscore.txt","w") as f:
        f.write(str(score))