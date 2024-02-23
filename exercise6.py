# Name of game is snake water game

import random

lst=["s","w","g"]

chance=int(input("enter no. of chance\n"))
no_of_chance=0
human_point=0
computer_point=0


print("\t \t \t \tSnake, Water ,Gun GAME")


while no_of_chance<chance:
    human=input("Snake, Water, Gun:\n")
    computer=random.choice(lst)


    if human==random:
        print("Tie both 0 point to each\n")

    elif human=="s" and computer=="g":
        computer_point=computer_point+1
        print(f"your guess {human} and computer guess {computer} \n")
        print("computers wins 1 point\n")
        print(f"computer point is {computer_point} and human point is {human_point}  \n")

    elif human=="s" and computer=="w":
        human_point=human_point+1
        print(f"your guess {human} and computer guess {computer}  \n")
        print("Human wins 1 point\n")
        print(f"computer point is {computer_point} and human point is {human_point} \n")


    elif human=="w" and computer=="s":
        computer_point=computer_point+1
        print(f"your guess {human} and computer guess {computer} \n")
        print("computer wins 1 point")
        print(f"computer point is {computer_point} and human point is {human_point} \n")


    elif human=="w" and computer=="g":
        human_point=human_point+1
        print(f"your guess {human} and computer guess {computer} \n")
        print("human wins 1 point")
        print(f"computer point is {computer_point} and human point is {human_point} \n")


    elif human=="g" and computer=="s":
        human_point=human_point+1
        print(f"your guess {human} and computer guess {computer} \n")
        print("human wins 1 point")
        print(f"computer point is {computer_point} and human point is {human_point} \n")

    elif human=="g" and computer=="w":
        computer_point=computer_point+1
        print(f"your guess {human} and computer guess {computer} \n")
        print("computer wins 1 point")
        print(f"computer point is {computer_point} and human point is {human_point} \n")



    else:
        print("your guess is wrong")

    no_of_chance=no_of_chance+1
    print(f"{chance-no_of_chance} is left out of {chance}")

print("Game Over")



if human_point==computer_point:
    print("Tie")

elif human_point>computer_point:
    print("I Won")

else:
    print("Computer Won")


print(f"your point is {human_point} and computer point is {computer_point} \n")
