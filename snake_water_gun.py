import random;
chance = 10
moves = 0
computer_win = 0
user_win = 0
print("WELCOME TO THE SNAKE WATER GAME")

while (moves < chance):
    user_move = (input("To choose your move please enter the choice(snake,gun,water): "))
    possible_choice = ["snake", "gun", "water"];
    computer_move = random.choice(possible_choice)
    if computer_move == user_move:
        print(f"your guess {user_move} and computer guess is {computer_move} ")
        print("BOTH THE PLAYERS CHOOSE SAME MOVE. IT IS A TIE!!")
    elif user_move == "snake":
        if computer_move == "gun":
            print(f"your guess {user_move} and computer guess is {computer_move} ")
            print("CONGRULATION!,GUN KILLS THE SNAKE.USER WIN!!")
            user_win = user_win+1
        else:
            print(f"your guess {user_move} and computer guess is {computer_move} ")
            print("SNAKE DRUNK THE WATER.COMPUTER WIN!!")
            computer_win = computer_win + 1

    elif user_move == "gun":
        if computer_move == "snake":
             print(f"your guess {user_move} and computer guess is {computer_move} ")
             print("CONGRULATION!,GUN KILLS THE SNAKE.COMPUTER WIN!!")
             computer_win = computer_win + 1
        else:
             print(f"your guess {user_move} and computer guess is {computer_move} ")
             print("CONGRULATION!,GUN DROWN IN THE WATER . USER WIN!!")
             user_win = user_win + 1

    elif user_move == "water":
        if(computer_move == "snake"):
             print(f"your guess {user_move} and computer guess is {computer_move} ")
             print("CONGRULATION!,SNAKE DRUNK THE WATER.USER WIN!! ")
             user_win = user_win + 1
        else:
            print(f"your guess {user_move} and computer guess is {computer_move} ")
            print("CONGRULATION!,GUN DROWN IN THE WATER . COMPUTER WIN!!")
            computer_win = computer_win + 1
    else:
        print("PLEASE!,Enter a valid move")
    moves = moves + 1;
    print(f"{chance - moves} is left out of {chance} \n")
print("GAME OVER!!")
if(computer_win == user_win):
    print(f"the computer wins {computer_win}   times and the user wins {user_win} times ")
    print("THE GAME IS TIE")
elif(computer_win > user_win):
    print(f"the computer wins {computer_win}   times and the user wins {user_win} times ")
    print("COMPUTER WINS THE GAME")
else:
    print(f"the computer wins {computer_win}   times and the user wins {user_win} times ")
    print("USER WINS THE GAME")
