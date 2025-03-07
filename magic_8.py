import random

question = input("Please enter your question: ")

num = random.randint(1, 9)

if num == 1:
    print("Yes")
elif num == 2:
    print("It is decidely so")
elif num == 3:
    print("Without a doubt")
elif num == 4:
    print("Reply hazy, try again")
elif num == 5:
    print("Ask again later")
elif num == 6:
    print("Better not tell you now")
elif num == 7:
    print("My sources say no")
elif num == 8:
    print("Outlook not good")
elif num == 9:
    print("Very doubtful")
else:
    print("Error")