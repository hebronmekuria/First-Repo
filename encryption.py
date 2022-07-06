#Hebron Mekuria
#September 28 2020
#Letters Exercise
with open("encrypted.txt","r+") as f:
 stringz=f.read()
 stringz=stringz.lower()


alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
newdict={}

def counting(str):
    
    for k in alphabet:
            count=0
            for i in stringz:
            
            
                
                if i==k:
                    count+=1
                    
            newdict[k]=count
            


counting(stringz)
print(newdict)
sorteddict=sorted(newdict.items(), key=lambda x:x[1], reverse=True) #I got this line of code from https://careerkarma.com/blog/python-sort-a-dictionary-by-value/#:~:text=To%20sort%20a%20dictionary%20by%20value%20in%20Python%20you%20can,Dictionaries%20are%20unordered%20data%20structures.
#I understood what it was doing for the most part except for the middle portion with key=...
vertical=[]
for i in sorteddict:
    vertical.append (i[0])
    
vertical=''.join(vertical)
print(vertical)








