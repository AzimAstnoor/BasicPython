try:
    import random
    rps = ["rock", "paper", "scissors"]
    spr = random.choice(rps)
    a = input("ENTER YOUR CHOICE")
    print("Computer Choice", spr)
    if spr == a:
        print("It's a Tie")
    elif spr == "rock" and a == "scissors":
        print("Computer Wins")
    elif spr == "rock" and a == "paper":
        print("You Win")
    elif spr == "scissors" and a == "paper":
        print("Computer Wins")
    elif spr == "scissors" and a == "rock":
        print("You Win")
    elif spr == "paper" and a == "rock":
        print("Computer Wins")
    elif spr == "paper" and a == "scissors":
        print("You Win")
except Exception as Z: print(Z)