import random
import time

print("""
***************************
Number guessing game

guess numbers from 1 to 40
***************************
""" )

random_number = random.randint(1,40)
guess_right = 7

while True:
    guess = int(input("please enter number:"))

    if (guess<random_number):
        print("information is being queried...")
        time.sleep(1)
        print("please enter a larger number")
        guess_right -=1
    elif (guess>random_number):
        print("information is being queried...") 
        time.sleep(1)
        print("please enter a smaller number")
        guess_right -=1
    else:
        print("information is being queried...")
        time.sleep(1)
        print("congratulations random number:",random_number)
        break
    if (guess_right == 0):
        print("you have no guesswork")
        break


