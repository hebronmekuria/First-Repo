#Hebron Mekuria
#Mystery Texts
#October 5, 2020

#The first text is a list of students in our class, with a full stop between their first and last names.
#The second text is from "The Argument Sketch" on MontyPython.net.
#The third text is from the T.V. show, Dr. Who.
#The fourth text is a piece from Ernest Vincent Wright's "A Story of Over 50,000 Words Without Using the Letter 'E'"
#The fifth text is from a news article about a baseball player and it was published on The News-Herald

def caesar(text,shift):
    shift=shift%26#This is to make sure that the function will only shift through the text 26 times or less. 
    text=text.lower()
    newtext=""
    for character in text:
        if 97<=ord(character)<=122: 
            if 97<=(ord(character)+shift)<=122:
                character=chr(ord(character)+shift)#This will be the next character, in the case that the new one doesn't go past 'z'
                
            else:
                character=chr(ord(character)+shift-123+97)
        else:
            character=character
        
        newtext=newtext+character
    return newtext

def checker(text,shift):
    

    shifted=caesar(text,shift)
    print(shifted)
    
    
    
    readability=input("Can you read this text? Type 'y' if you can, any other key if you can't.\n")
    
    if readability=='y' or readability=='Y':
        return True

    else:
        return False
    

def decode():
    
    textfile=input("Please enter the name of a file you want to decode. Please do not include .txt at the end of the name\n")
    with open("%s.txt"%textfile,"r+") as f: #This is a very useful line of code to include variables in the names of files
        filestring=f.read()
        for i in range (26):
            truth=checker(filestring, i)
            if truth==True:
                break
     
            


