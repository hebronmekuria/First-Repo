

#Hebron Mekuria
#Guessing Game, Project-1, CS 145B
#September 18, 2020
#In this game, a user is supposed to guess a number between 1 and 100 that is generated randomly.
#The code tells the user if their guess is too high, too low or correct.
#The users have an option of playing again and can have their names added to the scoreboard if they get the answer before running out of tries.

import random
import time

with open ("HighscoresHGM.txt", "w+") as f:
  f.write("3 User1\n")
  f.write("5 User2\n")
  f.write("1 User3\n")
  
#Open up a higscores file before getting started. The name has HGM at the end to make sure such file doesn't exist in the computer of whoever runs this, if it does, that file will be wiped!

print("Hey, there! Nice to meet you.")
playername=input("What's your name?\n")
print("Hey {}! Let's play a game\n".format(playername))#This ".format" command is used to enter variables into strings in an easier way
time.sleep(1)#This command delays the next line of code by the number of seconds in the () This makes python look less awkward and eager.
print("I've thought of a number between 1 and 100, and you try to guess it correctly in seven tries.\n")
time.sleep(1)
print("I will tell you if your guesses are too high, too low or correct.\n")
time.sleep(1)


def newgame():
  numberofgames=input("Please enter for the how manyth time you are playing. If it's your first, enter 1, if its your second, 2, etc.\n")
  #This is for later, to record their names with different numbers so that they can see their progress on the scoreboard
  shouldguess=random.randint(1,100) 
  
  

  
  print("Enter your first guess!")
  for i in range(7):
    n=6 

    
    try:
     playeranswer=int(input())
    
    except ValueError:
     
       
       print("Please only enter numerical values.Enter your guess again.\n")
       playeranswer=int(input())
    
  
    if (n-i)<0:
                     break 

      
      
    if playeranswer==shouldguess:
             
             score=n-i
             
             with open("HighscoresHGM.txt", "a+") as f:
               playerscore=str(n+1-i)
               appended=playerscore+" "+playername+numberofgames

               f.write("\n")
               f.write(appended)

               
               
               
             print("Ding, ding, ding! Nice Job! You are correct.")
             time.sleep(2)
             print("Score=the number of tries you had left when you got the correct answer")
             print("Your score is:", n+1-i,"!")
             time.sleep(2)
             
             
             
             
             with open("HighscoresHGM.txt", "r+") as f:
                 scoreboard=f.read().splitlines()
                 scoreboard.sort(reverse=True)
                 topthree=scoreboard[0:3]
                 
              #show the player the scoreboard as a list that is sorted from largest to smallest
             print("Here is the scoreboard:")
             for i in scoreboard:
                   print(i)
             print("Top three games:")
             for i in topthree:
                   print(i)
               
             time.sleep(3)
             print(" ")
             lastanswer=input("Play more games to improve your score! Do you want to play again(Y/N)\n")
               
             if lastanswer=="Y" or lastanswer=="y":
                newgame()
             else:
                 print("Goodbye! Thanks for playing.")
                 exit()
                  
    elif playeranswer>shouldguess:
                     
                     
                       print("Too high! You have",n-i,"tries left.")
                     
                     
                     
                     
    elif playeranswer<shouldguess:
                     
                     print("Too low! You have",n-i, "tries left.")

    
  print("You lost!")
  time.sleep(1.8)
  print("The correct answer was {}".format(shouldguess))
  time.sleep(1.8)
  score=n+1-i
  print("Score=the number of tries you had left when you got the correct answer")
  print("Your score is {}".format(score))
  
           
  with open("HighscoresHGM.txt", "r+") as f:
      scoreboard=f.read().splitlines()
      scoreboard.sort(reverse=True)
      topthree=scoreboard[0:3]
  print("Here is the scoreboard:")
  for i in scoreboard:
                 print(i)
  print("The top three players are:")
  for i in topthree:
                 print(i)
             

  

  time.sleep(1)
  lastanswer=input(("Do you want to play again? Maybe you'll make it on the scoreboard next time.(Y/N)\n"))
  if lastanswer=="Y" or lastanswer=="y":
    newgame()
  else:
               print("Goodbye{}! Thanks for playing.".format(playername))
               exit()
   

newgame()
                   

