import random
from time import sleep as delay


def square():
    global count
    print(f"The data type of {name} is {type(name)}")
    question = random.randint(1, 100)
    ans = question * question
    print(f"What is the square of {question}?")
    Answer = int(input())
    if (ans == Answer):

        print(f"The data type of {Answer} is {type(Answer)}")
        # print("WHat is the square of {question}?")
        count = count + 1
        print("Your answer is right")
    else:
        count = 0
        print("Your answer is wrong")

    if (count == 3):
        print(f"{name} won the game , Congratulations")
        delay(10)
        return

    else:
        print("Do you want to continue?Continue:1 Exit:0")
        ans = int(input())

        if (ans == 1):
            square()
        else:
            print(f"{name} is Loser")
            return 0


def squareroot():
    global count
    print(f"The data type of {name} is {type(name)}")
    question = random.randint(1, 10000)
    # question=12
    ans = question * question
    print(f"What is the square root of {question}?")
    Answer = int(input())
    if (ans == Answer):

        print(f"The data type of {Answer} is {type(Answer)}")
        # print("What is the square root of {question}?")
        count = count + 1
        print("Your answer is right")
    else:
        count = 0

        print("Your answer is wrong")

    if (count == 3):
        print(f"{name} won the game , Congratulations")
        delay(10)
        return

    else:
        print("Do you want to continue?Continue:1 Exit:0")
        ans = int(input())

        if (ans == 1):
            squareroot()
        else:
            print(f"{name} is Loser")
            return 0


name = input("Please enter your name:")
print("Hi", name, "Welcome to play the Game")
count = 0
'''while(count!=3):
permission = int(input('Would you like to start? (Square):1 (Squareroot):0'))
if(permission==1):
    square()
else:
    squareroot()'''

functions = [square(), squareroot()]
for _ in range(3):
    random.choice(functions)()















