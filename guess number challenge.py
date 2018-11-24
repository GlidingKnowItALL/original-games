import random

import time



def start():
    print("Hi, lets guess the number!")
    
    game()



def game():
    
    tries = 0
    number = random.randint(0, 1000)
    
    while True:
        answer = input(":  ")
        tries += 1
        tall = int(answer)

        if tall == number:
            print("You did it!")
            break

        if tall > number:
            print("the answer is less.")

        if tall < number:
            print("the answer is more.")

            
    print("You tried {} times!".format(tries))
    
    if tries > 9:
        print("Better luck next time.")

        
    if tries == 1:
        print("WOW! YOU DID IT IN ONE TRY!")

        
    if tries > 5:
        
        if tries < 10:
            print("You did great!")
            

    if tries > 1:
        
        if tries < 5:
            print("Nice!")

            
    time.sleep(2)
    print ("loading new game...")
    time.sleep(3)
    print("We got a new number!")
    game()

    
start()
