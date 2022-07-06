#Hebron Mekuria 
#Project2: Inspirational Texts
#October 6, 2020
#In this code, the user has the option of performing muliple tasks with a certain text.
#The user is given a menu where they can choose to find how many times a word or phrase occurs in the file, to see the conext of a certain word or phrase
#to find and replace within the file, to encode the file and save the encoded version in a new file, to play a guessing game with the code, and to send an email to themselves that contains a certain word or phrase, or to send a random chunck of text

import time
import random
print("Hey there!")
print(" ")

print("Please enter the name of the file you want to work on. Please do NOT include .txt at the end of the name.")
while True:
  try: 
    textfile=input()

    with open("%s.txt"%textfile,"r+") as f: #this command is useful to enter variables in the names of files
      filestring=f.read()
    break
      
  except:
      
      
       print("Sorry, we couldn't find the file you requested. Please try again.\n")
       continue
       
while True:
  print("Here's a list of what you can do with the file.","1. Find out how many times a word/phrase occurs in the file.", "2. See the context of a word/phrase of your choice.","3. Perform a search and replace.","4. Encode the file.","5. Play a game with me!","6. Send an email." , sep="\n")
  print(" ")
  try:
   userchoice=int(input("From the above menu, please choose the corresponding number of what you would like to do. For example, if you want to do a search and replace, press 3.\n"))
  except:
      userchoice=int(input("Please enter the correct numerical value corresponding with your choice.\n"))
                     
  if userchoice==1:

   #2a
   tocount=input("Please enter the name of the word or phrase you would like to search for. You do not need to put quotes around it.\n")
   counting=filestring.count(tocount) #this method returns the number of occurences of the string inside the bracket as found in the initially mentioned string
   print('"',tocount,'"'," occurs ",counting," times.", sep="")
   continuing=input("Would you like to see the menu again? (y/n)")
   if continuing=='y' or continuing=='Y':
     continue
   else:
     break
   
   
  elif userchoice==2:
   #2b 
   context=input("Please enter the word or phrase for which you would like to see context.\n")
   isitthere=filestring.count(context)
   if isitthere==0:
     print("Sorry, your chosen word/phrase doesn't occur within the file.")
   else:
     where=filestring.find(context)
     print(filestring[where-100:where+101]) # The context here will contain the 100 characters before and after the requested word or phrase
   continuing=input("Would you like to see the menu again? (y/n)")
   if continuing=='y' or continuing=='Y':
     continue
   else:
     break
   
  elif userchoice==3:
   #2c
   whattosearch=input("For the search and replace, which word or phrase would you like to search for?\n")
   whattoreplace=input("For the search and replace, what would you like the replacement to be?\n")
   filestringreplaced=filestring.replace(whattosearch, whattoreplace)
   with open("textreplaced.txt","w+") as f: #Here, I am saving the new string with the search and replace done on it to a new file.
     f.write(filestringreplaced)
   
   print("Your search and replace was successful. The new string with the replaced items is saved in a file titled 'textreplaced.txt'.") #create a new next text file with the replacement taken place
   continuing=input("Would you like to see the menu again? (y/n)")
   if continuing=='y' or continuing=='Y':
     continue
   else:
     break
  elif userchoice==4:

      #2d

      def caesar(text,shift):
          shift=shift%26 #this makes sure that the shift occurs only 26 times or less 
          text=text.lower()
          newtext=""
          for character in text:
              if 97<=ord(character)<=122:#makes sure that the character is an alphabet, because if it isn't there is no need to involve it in the encoding
                  if 97<=(ord(character)+shift)<=122: #makes sure that the shifted character is still a lowercase alphabet
                      character=chr(ord(character)+shift)
                      
                  else:
                      character=chr(ord(character)+shift-123+97)
              else:
                  character=character
              
              newtext=newtext+character
          return newtext
      encodedfile=caesar(filestring, 5) #'5' is an arbitrary choice by which the characters are shifted and the text is encoded
      with open("newencodedfile.txt","w+") as f:
          f.write(encodedfile)
      print("Your file has been encoded and saved into a new file. The name of the new file is newencodedfile.txt.\n")
      continuing=input("Would you like to see the menu again? (y/n)")
      if continuing=='y' or continuing=='Y':
        continue
      else:
        break
  elif userchoice==5:
      #2e
      print("Let's play a game.")
      time.sleep(0.5)
      print("Give me a word or phrase which you think might occur in the file. We will both guess the number of times that the word or phrase occurs.")
      print("Whoever has the closest guess wins!")
      time.sleep(1)
      toguess=input("Enter the word/phrase to get started.\n")
      myguess=random.randint(10,1000) 
      print("My guess is",myguess)
      theirguess=int(input("What is your guess?"))
      counting=filestring.count(toguess)
      print('"',toguess,'"'," occurs ",counting," times.", sep="")
      if abs(counting-myguess)<abs(counting-theirguess): #the abs function helps to find the gap between the two numbers, no matter which one is greater
          print ("I win!")
          
      elif abs(counting-myguess)==abs(counting-theirguess):
          print("We tied! Nice game.")
      else:
          print("You win! Nice job!")
      
      continuing=input("Would you like to see the menu again? (y/n)")
      if continuing=='y' or continuing=='Y':
        continue
      else:
        break
  elif userchoice==6:
     #Starter code from https://medium.freecodecamp.org/send-emails-using-code-4fcea9df63f
     #Info on ports here: https://support.desk.com/customer/portal/articles/1741-configuring-smtp-servers-to-send-email

     import smtplib, random
     from email.mime.multipart import MIMEMultipart
     from email.mime.text import MIMEText
     whattoemail=int(input("Would you like to email a random chunk of the text or a portion of the text containing a specific word? Type 1 for random and 2 for speciifc word.\n"))
     if whattoemail==1:
       startingpoint=random.randint(1,10000)
       endingpoint=random.randint(1,10000)
       starting=min(startingpoint, endingpoint)
       ending=max(startingpoint, endingpoint)
       whattosend=filestring[starting:ending+1]
       
     else:
       whatword=input("What word would you like the email to contain?\n")
       where=filestring.find(whatword)
       howbig=random.randint(1,500)
       whattosend=filestring[where-howbig:where+howbig] #this code decides what the scope of the text surrounding the chosen word or phrase will be

     
       
     
     #Starter code from https://medium.freecodecamp.org/send-emails-using-code-4fcea9df63f
     #Info on ports here: https://support.desk.com/customer/portal/articles/1741-configuring-smtp-servers-to-send-email
     def sendEmail(sender, sendee, header, body, password):
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(sender, password)
        msg = MIMEMultipart()
        msg['From']= sender
        msg['To']= sendee
        msg['Subject']= header
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
        del msg
        s.quit()
     while True:
       theiremail=input("Please enter your email.")
       try:
         sendEmail("hebronnewemail@gmail.com",theiremail,"This is an email from Python.",whattosend,"hypsincos30")
         print("Your email has been sent.")
         break
       except:
         print("Sorry, we could not send you an email. Please re-check your email and your internet connection.")
         continue
     time.sleep(0.5)
     continuing=input("Would you like to see the menu again?(y/n)")
     if continuing=='y' or continuing=='Y':
        continue
     else:
        break
  else:
    print("Please enter a valid numeral that corresponds to an item in the above menu.")
    continue
  
        
    
print("Alright then, goodbye!")

