# Uses python3
import sys
from GameBoard import GameBoard


def draw_state(candy_state):
    i = 0
    print("\n")
    for ic in candy_state:
        if ic == "e":
            print(" ", end="      ")
        else:
            print(ic, end="      ")
        i += 1
        if i == 5:
            i = 0
            print("\n")


def game_input():
    move = input("Enter Move : ")
    current_tile_possible_moves = empty_tile.get_possible_moves()
    for possible_move in current_tile_possible_moves:
        if move.upper() == possible_move or move.lower() == possible_move:
            print("move tile")
            move_tile(move)
            return
    print("Not a valid move.")


def move_tile(move):
    if move == "U" or move == "u":
        neighbour_tile = empty_tile.get_candy_object_up()
        empty_tile.set_candy_value(neighbour_tile)
    elif move == "D" or move == "d":
        print("Move Down")
    elif move == "L" or move == "l":
        print("Move Left")
    elif move == "R" or move == "r":
        print("Move Right")


def set_possible_movies_for_all_tiles():
    tileA.set_possible_moves(["L", "U"])
    tileB.set_possible_moves(["L", "R", "U"])
    tileC.set_possible_moves(["L", "R", "U"])
    tileD.set_possible_moves(["L", "R", "U"])
    tileE.set_possible_moves(["R", "U"])
    tileF.set_possible_moves(["L", "U", "D"])
    tileG.set_possible_moves(["L", "R", "U", "D"])
    tileH.set_possible_moves(["L", "R", "U", "D"])
    tileI.set_possible_moves(["L", "R", "U", "D"])
    tileJ.set_possible_moves(["R", "U", "D"])
    tileK.set_possible_moves(["L", "D"])
    tileL.set_possible_moves(["L", "R", "D"])
    tileM.set_possible_moves(["L", "R", "D"])
    tileN.set_possible_moves(["L", "R", "D"])
    tileO.set_possible_moves(["R", "D"])


def set_neighbor_tiles():

    # TileA
    tileA.set_candy_object_up(tileF)
    tileA.set_candy_object_left(tileB)

    # TileB
    tileB.set_candy_object_left(tileC)
    tileB.set_candy_object_right(tileA)
    tileB.set_candy_object_up(tileG)

    # TileC
    tileC.set_candy_object_left(tileD)
    tileC.set_candy_object_right(tileB)
    tileC.set_candy_object_up(tileH)

    # TileD
    tileD.set_candy_object_left(tileE)
    tileD.set_candy_object_right(tileC)
    tileD.set_candy_object_up(tileI)

    # TileE
    tileE.set_candy_object_right(tileD)
    tileE.set_candy_object_up(tileJ)

    # TileF
    tileF.set_candy_object_up(tileK)
    tileF.set_candy_object_right(tileG)
    tileF.set_candy_object_down(tileA)

    # TileG
    tileG.set_candy_object_right(tileF)
    tileG.set_candy_object_down(tileB)
    tileG.set_candy_object_up(tileL)
    tileG.set_candy_object_left(tileH)

    # TileH
    tileH.set_candy_object_right(tileG)
    tileH.set_candy_object_down(tileC)
    tileH.set_candy_object_up(tileM)
    tileH.set_candy_object_left(tileI)

    # TileI
    tileI.set_candy_object_right(tileH)
    tileI.set_candy_object_down(tileD)
    tileI.set_candy_object_up(tileN)
    tileI.set_candy_object_left(tileJ)

    # TileJ
    tileJ.set_candy_object_right(tileI)
    tileJ.set_candy_object_down(tileE)
    tileJ.set_candy_object_up(tileO)

    # TileK
    tileK.set_candy_object_down(tileF)
    tileK.set_candy_object_left(tileL)

    # TileL
    tileL.set_candy_object_left(tileM)
    tileL.set_candy_object_right(tileK)
    tileL.set_candy_object_down(tileG)

    # TileM
    tileM.set_candy_object_left(tileN)
    tileM.set_candy_object_right(tileL)
    tileM.set_candy_object_down(tileH)

    # TileN
    tileN.set_candy_object_left(tileO)
    tileN.set_candy_object_right(tileM)
    tileN.set_candy_object_down(tileI)

    # TileO
    tileO.set_candy_object_down(tileJ)
    tileO.set_candy_object_right(tileN)


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

    # Create object per each Tile.
    tileA = GameBoard(input_candies[0],"A")
    tileB = GameBoard(input_candies[1],"B")
    tileC = GameBoard(input_candies[2],"C")
    tileD = GameBoard(input_candies[3],"D")
    tileE = GameBoard(input_candies[4],"E")
    tileF = GameBoard(input_candies[5],"F")
    tileG = GameBoard(input_candies[6],"G")
    tileH = GameBoard(input_candies[7],"H")
    tileI = GameBoard(input_candies[8],"I")
    tileJ = GameBoard(input_candies[9],"J")
    tileK = GameBoard(input_candies[10],"K")
    tileL = GameBoard(input_candies[11],"L")
    tileM = GameBoard(input_candies[12],"M")
    tileN = GameBoard(input_candies[13],"N")
    tileO = GameBoard(input_candies[14],"O")

    # Setup initial board with given input
    set_possible_movies_for_all_tiles()
    set_neighbor_tiles()

    tile_object_lst = [tileA, tileB, tileC, tileD, tileF, tileG, tileH, tileI, tileJ, tileK, tileM, tileN, tileO]

    for tile_object in tile_object_lst:
        if tile_object.get_candy_value() == "e":
            empty_tile = tile_object
    test = empty_tile.get_candy_object_left()

    game_input()
