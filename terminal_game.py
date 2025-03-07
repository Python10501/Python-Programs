import time
import random

#This is where the game asks for you to choose a name for your character
print("Day in the Life")
time.sleep(2)
print("In this game you will control the daily life of a chacter")
time.sleep(2)
name = input("Give you character a name: ")
time.sleep(2)
print(f"You have given you character the name {name}")
time.sleep(2)
start = input("Would you like to start the game? Enter yes or no: ")

#this if statment either starts the game or exits the game.
if start == "yes":
    time.sleep(1)
    print("The game has been started, thanks for playing \n")
    time.sleep(2)

elif start == "easter-egg":
    time.sleep(1)
    print("https://www.youtube.com/watch?v=xvFZjo5PgG0")
    time.sleep(1)
    print("Trust me the link is safe, I wouldn't have put it in if it wasn't, I work in I.T doing network security")
    exit()

else:
    time.sleep(2)
    print("Ok, see you around, bye bye")
    exit()

print("Your alarm wakes you up out of your sleep as you have to get ready for your new job in Data Science.")
time.sleep(2)
print("You hop out of bed and you have laid out two different outfits for you to wear to your new job.")
time.sleep(2)
print("You have a outfit with a white hoodie and blue jeans and a outfit with a blue hoodie and black jeans, which one do you wanna wear:? ")
time.sleep(2)
#This input and if statement allows you to choose and outfit for your character
clothes = int(input("type 1 for the white hoodie and blue jeans or 2 for the blue hoodie and black jean: "))
if clothes == 1:
    time.sleep(2)
    print(f"You have decided to wear the white hoodie and blue jeans, this outfit looks good on you {name}.\n")
    time.sleep(2)

elif clothes == 2:
    time.sleep(2)
    print(f"You have decided to wear the blue hoodie and black jeans, this outfit looks good on you {name}.\n")
    time.sleep(2)

elif clothes == 1 or clothes == 2:
    print("Error: Invalid Input")

print("After you pick the outfit you want to wear for the day and grab a quick breakfast from the fridge, you start your journey to your new job.")
time.sleep(2)
print("However you need to decide whether you want to take your own vehicle or public transport.")
time.sleep(2)

#This if statement allows the user to choose how they get to their new job
transport = input("Please type in either bus or car to choose your transportation: ")
if transport == "car":
    time.sleep(2)
    print("You have choosen to take your own vehicle, this is a lot faster and you won't have to pay a bus fee and you will get to work a lot eariler.\n")
    time.sleep(2)

elif transport == "bus":
    time.sleep(2)
    print("Before you think about taking the bus, you check you wallet to make sure you can pay for the bus.")
    time.sleep(2)
    print("You find out that the bus fee is usually around 4 USD in your city.")
    time.sleep(2)
    print("You find that you have 6 USD in your wallet so you are able to pay for the bus and are able to make it to work on time.\n")
    time.sleep(2)
else:
    print("Error: Invaild Input")
    exit()


print("You finally arrive at your new job, you walk inside and find you way to you new office and begin setting up your things.")
time.sleep(2)
print("You take out your laptop, some paper to do calculations on if need be, along with other office supplies and also a magic 8 ball to play with incase there is nothing to do.")
time.sleep(2)
print("While at your desk you can either start your work or play with the magic 8 ball.")
time.sleep(2)
action = input("What do you choose to do, type work to begin working or type magic to play with the magic 8 ball: ")
time.sleep(2)

#this if statement lets the player choose what they do at work
if action == "work":
    print("You begin working and cleaning some data from a CSV file that was sent to you in an email.")
    time.sleep(2)
    print("After a couple of hours or so, you were able to clean up the data and code some pie charts and box-plots for the data.\n")
#This begins the magic 8 ball program
elif action == "magic":
    print("You begin to play with the magic 8 ball instead of working, tsk tsk.\n")
    time.sleep(2)

    question = input("Please enter your question: ")
    print("shake")
    time.sleep(2)
    print("shake")
    time.sleep(2)
    print("shake")

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
        print("Error: Invalid Input")
        exit()

    time.sleep(2)
    print("You think to youself that you probably shouldn't be playing around on your first day at your new job.")
    time.sleep(2)
    print("You put the magic eight ball down and begin your work")
    time.sleep(2)
    print("You begin working and cleaning some data from a CSV file that was sent to you in an email.")
    time.sleep(2)
    print("After a couple of hours or so, you were able to clean up the data and code some pie charts and box-plots for the data.\n")
    time.sleep(2)

print(f"After a long day of hard work, its time from you to go back home. You return to the {transport} and begin your journey home.")
time.sleep(2)
print("Once back home you decide to relax by playing some video games")
time.sleep(2)
print("You are stuck on which game you want to play, you can either play Minecraft or maybe some SpaceMarine 2.")
time.sleep(2)
game = input("Type craft to choose Minecraft or type bolter to play SpaceMarine 2: ")

#This if statement allows the player to choose what game they want to play
if game == "craft":
    print("You open up Minecraft on your computer and make a new world to explore.")
    time.sleep(1)
    print("After playng for a few hours you relize that you should probably get cleaned up and go to bed as you start your second day tommrow at your new job.\n")
    time.sleep(2)
elif game == "bolter":
    print("You open up SpaceMarine 2 in your steam libary and decide to slay some xenos for the God Emperior of Mankind.")
    time.sleep(2)
    print("After playng for a few hours you relize that you should probably get cleaned up and go to bed as you start your second day tommrow at your new job.\n")
    time.sleep(2)
else:
    print("Error: Invalid Input")
    exit()

#End of the program
print("Thanks for playing my small Day in the Life game")
time.sleep(2)
print("Feel free to restart the program to choose some different answers...")
time.sleep(2)