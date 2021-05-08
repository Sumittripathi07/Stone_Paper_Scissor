import random
i = 0
while (True):
    go = ["stone", "paper", "scissor"]
    comp = random.choice(go)
    user =input("s for stone,p for paper,c for scissor----> ")

    print("Computer--->",comp)
    if user =="s" and comp =="paper":
        print("you lose")
    elif user == "s" and comp =="stone":
        print("Match Draw")
    elif user == "s" and comp =="scissor":
        print("you won")    

    elif user =="p" and comp =="paper":
        print("Match Draw")
    elif user == "p" and comp =="stone":
        print("You Won")
    elif user == "p" and comp =="scissor":
        print("You lose")    

    elif user =="c" and comp =="paper":
        print("You won")
    elif user == "c" and comp =="stone":
        print("You lose")
    elif user == "c" and comp =="scissor":
        print("Match Draw")
    continue
