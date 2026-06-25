print("Welcome to Rock Paper Scissor Game ")
l=["rock","paper","scissor"]

user_move=input("enter the move: ")
if user_move not in l:
    print("invalid input")
else:
    print("user move->",user_move)
    import random
    cp_move=random.choice(l)
    print("computer move->",cp_move)

    if user_move==cp_move:
        print("it's a tie")
    elif user_move=="rock" and cp_move=="scissor":
        print("user wins")
    
    elif user_move=="paper" and cp_move=="rock":
        print("user wins")
    elif user_move=="scissor" and cp_move=="paper":
        print("user wins")
    else:
        print("computer wins")

    print("thank you for playng")
    print("see you soon")







