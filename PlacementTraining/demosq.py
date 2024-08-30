import random
from time import sleep as delay
import math


def square():
    global count

    question = random.randint(1, 100)
    ans = question * question
    print(f"What is the square of {question}?")
    Answer = int(input())
    if (ans == Answer):

        # print("WHat is the square of {question}?")
        count = count + 1
        print("Your answer is right")
        return 0
    else:
        count = 0
        print("Your answer is wrong")
        return 0

    '''
    if(count==3):
        print(f"{name} won the game , Congratulations")
        delay(10)


    else:
        print("Do you want to continue?Continue:1 Exit:0")
        ans = int(input())

        if(ans==1):
            square()
        else:
            print(f"{name} is Loser")
            return 0'''


def squareroot():
    global count
    question = random.randint(1, 100)
    # question=144
    question1 = question * question
    print(f"What is the square root of {question1}?")
    Answer = int(input())

    if (question == Answer):

        # print("What is the square root of {question}?")
        count = count + 1
        print("Your answer is right")
        return 0
    else:
        count = 0

        print("Your answer is wrong")
        return 0

    '''if(count==3):
        print(f"{name} won the game , Congratulations")
        delay(10)
        return

    else:
        print("Do you want to continue?Continue:1 Exit:0")
        ans = int(input())

        if(ans==1):
            squareroot()
        else:
            print(f"{name} is Loser")
            return 0'''


name = input("Please enter your name:")
print("Hi", name, "Welcome to play the Game")
count = 0
while (count != 3):
    rand = random.randint(0, 1)
    if (rand == 1):
        square()
    else:
        squareroot()
    if (count == 3):
        print(f"{name} won the game , Congratulations")
        delay(5)


    else:
        print("Do you want to continue?Continue:1 Exit:0")
        ans = int(input())

        if (ans == 1):
            squareroot()
        else:
            print(f"{name} is Loser")
            exit()
'''permission = int(input('Would you like to start? (Square):1 (Squareroot):0'))
if(permission==1):
    square()
else:
    squareroot()'''

'''functions=[square(),squareroot()]
for _ in range(3):
    random.choice(functions)()'''















