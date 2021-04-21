import random 
a = random.randint(0,10)


for i in range (5):
    b = int(input('Guess a number between 0 and 10'))
    if(a==b):
        print('You win')
        break
    elif(a<b):
        print('Your guess was higher than the number')
   
    else:
        print('Your guess was lower than the number') 
    
    print ("you have", (6-i), "lives left")
if (a!=b):
    print ("you lose!!")