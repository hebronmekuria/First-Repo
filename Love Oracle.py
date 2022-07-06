

#Hebron Mekuria
#Love Oracle Assignment
#September 21, 2020
#This code takes the name of two lovers and returns how compatable they are.
#The calculation is done by: giving each name five points for the number of vowels it has and taking away one point for each consonant it has.
#Then finally, the calculation results for the two names are assessed and if their difference is five or less, they are deemed soul mates, six to ten:decent match and
#over ten, their relationship is hopeless.
import time
import sys
def love_oracle():
    
    print("Are you ready to find out if you and your partner are meant to be?")
    time.sleep(1.5)      
    string1=input("Enter your name\n")
    string2=input("Enter your partner's name\n")
    print("Drumroll!")
    time.sleep(1)

    for i in range (5,0,-1):
        print (i)
        time.sleep(0.5)
        
        
    vowelcount=0
    consonantcount=0
    for i in string1:
        
        vowels=["a","e","i","o","u","A","E","I","O","U"]
        if i in vowels:
            vowelcount+=5
        else:
            consonantcount+=1
    string1score= vowelcount-consonantcount
        

    vowelcount=0
    consonantcount=0
    for i in string2:
       
        vowels=["a","e","i","o","u","A","E","I","O","U"]
        if i in vowels:
            vowelcount+=5
        else:
            consonantcount+=1
    
    string2score=vowelcount-consonantcount

    if -5<=string1score-string2score<=5:
        print("Soulmates! Love is in the air.")
    elif 6<=(string1score-string2score)<=10 or -10<=(string1score-string2score)<=6:
        print("You're a decent match.")
    else:
        print("We're sorry, it wasn't meant to be. Try elsewhere!")
    time.sleep(1.5)
    again=input("Would you like to try again? (Y/N)\n")

    while True:
        if again=="y" or again=="Y":
            love_oracle()
        else:
            print("Goodbye! Thanks for playing")
            sys.exit()
            
        
love_oracle()
