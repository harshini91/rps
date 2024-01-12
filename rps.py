from random import randint
#create a list of play options
t=["Rock","Paper","Scissor"]
#assign a random play to the computer
computer=t[randint(0,2)]
#set player to false
player=False
while player==False:
    player = input("Rock,Paper,Scissor?:")
    if player==computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("you lose!",computer,"covers",player)
        else:
            print("you win!",player,"smashes",computer)
    elif player=="Paper":
        if computer=="Scissors":
            print("you loose!",computer,"cut",player)
        else:
            print("you win!",player,"covers",computer)
    elif player=="Rock":
        if computer=="Scissor":
            print("you win!",player,"smashes",computer)
        else:
            print("you lose!",computer,"covers",player)
    else:
        print("That's not a vadil play.check your spelling")
    player=False
    computer=t[randint(0,2)]
