# Uses python3
from GameBoard import GameBoard
import os

sequence_of_move = None
all_solution_path = 0


# Method to display the candy box after each move
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


# Check goal state after each move
# Return True if it has reached at Goal State else False
def check_goal_state():
    global sequence_of_move
    global all_solution_path
    a_to_e = tileA.get_candy_value() + tileB.get_candy_value() + tileC.get_candy_value() + tileD.get_candy_value() + tileE.get_candy_value()
    k_to_o = tileK.get_candy_value() + tileL.get_candy_value() + tileM.get_candy_value() + tileN.get_candy_value() + tileO.get_candy_value()

    if a_to_e == k_to_o:
        print("You Won..!!")
        output_file.write(sequence_of_move + "\n")
        output_file.write(str(len(sequence_of_move.replace(" ", ""))) + "\n")
        all_solution_path += len(sequence_of_move.replace(" ", ""))
        return True
    else:
        return False


# Take input(U, D, L, R) and check for legal or illegal move
def game_input():
    move = input("Enter Move : ")
    current_tile_possible_moves = empty_tile.get_possible_moves()
    for possible_move in current_tile_possible_moves:
        if move.upper() == possible_move or move.lower() == possible_move:
            # print("move tile")
            move_tile(move)
            return
    print("Not a valid move.")


# Move candy tile if the input is valid
def move_tile(move):
    global empty_tile
    global sequence_of_move

    if move == "U" or move == "u":
        neighbour_tile = empty_tile.get_candy_object_up()
        sequence_of_move = sequence_of_move + " " + neighbour_tile.get_tile_name()
        empty_tile.set_candy_value(neighbour_tile.get_candy_value())
        neighbour_tile.set_candy_value("e")
        empty_tile = neighbour_tile
    elif move == "D" or move == "d":
        neighbour_tile = empty_tile.get_candy_object_down()
        sequence_of_move = sequence_of_move + " " + neighbour_tile.get_tile_name()
        empty_tile.set_candy_value(neighbour_tile.get_candy_value())
        neighbour_tile.set_candy_value("e")
        empty_tile = neighbour_tile
    elif move == "L" or move == "l":
        neighbour_tile = empty_tile.get_candy_object_left()
        sequence_of_move = sequence_of_move + " " + neighbour_tile.get_tile_name()
        empty_tile.set_candy_value(neighbour_tile.get_candy_value())
        neighbour_tile.set_candy_value("e")
        empty_tile = neighbour_tile
    elif move == "R" or move == "r":
        neighbour_tile = empty_tile.get_candy_object_right()
        sequence_of_move = sequence_of_move + " " + neighbour_tile.get_tile_name()
        empty_tile.set_candy_value(neighbour_tile.get_candy_value())
        neighbour_tile.set_candy_value("e")
        empty_tile = neighbour_tile

    new_state = []
    for new_tile_object in tile_object_lst:
        new_state.append(new_tile_object.get_candy_value())
    draw_state(new_state)


# Set possible moves for each candy tile
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


# Set neighbour tiles for each candy tiles
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
    tileF.set_candy_object_left(tileG)
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

    print("Use Following commands to move Candies.")
    print("Up : U/u")
    print("Down : D/d")
    print("Right : R/r")
    print("Left : L/l")

    output_file = open("output.txt", "w+")

    selection = input("1.Automatic or 2.Manual: ")
    # if selection == "2":

    if selection == "1":
        print("Automatic")
        os.system("python3 automatic_mode.py")
    else:
        for ls in lst:
            sequence_of_move = None
            input_candies = []
            for ip in ls:
                if ip != " ":
                    input_candies.append(ip)

            draw_state(input_candies)
            print("")

            # Create object per each Tile.
            tileA = GameBoard(input_candies[0], "A")
            tileB = GameBoard(input_candies[1], "B")
            tileC = GameBoard(input_candies[2], "C")
            tileD = GameBoard(input_candies[3], "D")
            tileE = GameBoard(input_candies[4], "E")
            tileF = GameBoard(input_candies[5], "F")
            tileG = GameBoard(input_candies[6], "G")
            tileH = GameBoard(input_candies[7], "H")
            tileI = GameBoard(input_candies[8], "I")
            tileJ = GameBoard(input_candies[9], "J")
            tileK = GameBoard(input_candies[10], "K")
            tileL = GameBoard(input_candies[11], "L")
            tileM = GameBoard(input_candies[12], "M")
            tileN = GameBoard(input_candies[13], "N")
            tileO = GameBoard(input_candies[14], "O")

            # Setup initial board with given input
            set_possible_movies_for_all_tiles()
            set_neighbor_tiles()

            tile_object_lst = [tileA, tileB, tileC, tileD, tileE, tileF, tileG, tileH, tileI, tileJ, tileK, tileL,
                               tileM,
                               tileN, tileO]

            for tile_object in tile_object_lst:
                if tile_object.get_candy_value() == "e":
                    empty_tile = tile_object

            while not check_goal_state():
                game_input()
        output_file.write(str(all_solution_path))
