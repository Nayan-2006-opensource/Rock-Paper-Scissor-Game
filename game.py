print("Welcome to Rock Paper Scissor Game ")
l=["rock","paper","scissor"]
user_score=0
cp_score=0
while True:
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
            user_score=user_score+1
            cp_score=cp_score+1

        elif user_move=="rock" and cp_move=="scissor":
            print("user wins")
            user_score=user_score+1
    
        elif user_move=="paper" and cp_move=="rock":
            print("user wins")
            user_score=user_score+1

        elif user_move=="scissor" and cp_move=="paper":
            print("user wins")
            user_score=user_score+1

        else:
            print("computer wins")
            cp_score=cp_score+1
            

        print("user score->",user_score)
        print("computer score->",cp_score)
        
        if user_score==3:
            print("user wins")
        if cp_score==3:
            print("computer wins")
        
    if user_score==3 or cp_score==3:
        print("thanks for playing")
        print("see u soon")
        break
    
    



    









