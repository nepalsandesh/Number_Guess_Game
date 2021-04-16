#random module
from random import randint

x = int(input("Enter the 1st number"))

y = int(input("Enter The 2nd number")) 

ans= randint(x,y)

guess = int(input("Enter the number you guess"))


count=0

while guess!=ans:
    


    if guess>ans:
        guess=int(input("Try samller number"))
        count = count +1  
        

    if guess<ans:
        guess=int(input("try greater number"))
        count = count +1  

    if guess==ans:
        print("Congratulations. You passed in", count,'attempt')
        break
    count = count +1        
       




