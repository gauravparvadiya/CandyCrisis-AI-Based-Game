# Uses python3
import sys


def draw_state(candy_state):
    i = 0
    print("\n")
    for ic in candy_state:
        if ic == "e":
            print(" ",end="      ")
        else:
            print(ic, end="      ")
        i += 1
        if i == 5:
            i = 0
            print("\n")


def game_play():
    move = input("Enter Move : ")
    if move == "U" or move == "u":
        print("move up")
    elif move == "D" or move == "d":
        print("Move Down")
    elif move == "L" or move == "l":
        print("Move Left")
    elif move == "R" or move == "r":
        print("Move Right")
    else:
        print("Command not found.")


if __name__ == "__main__":
    lst = list(open("Sample_Data.txt"))
    input_candies = []
    for ip in lst[0]:
        if ip != " ":
            input_candies.append(ip)
    print("Use Following commands to move Candies.")
    print("Up : U/u")
    print("Down : D/d")
    print("Right : R/r")
    print("Left : L/l")

    draw_state(input_candies)
    print("")
    game_play()
