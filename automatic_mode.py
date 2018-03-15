# Uses python3
from GameBoard import GameBoard
from GameNode import GameNode
import timeit

open_list = []
# closed_list = []


# Check goal state after each move
# Return True if it has reached at Goal State else False
def check_goal_state(current_node):
    global all_solution_path
    current_node_setup = current_node.get_node_candy_setup()
    i = 0
    a_to_e = ""
    k_to_o = ""
    for candy in current_node_setup:
        if i < 5:
            a_to_e = a_to_e + candy
        elif i > 9:
            k_to_o = k_to_o + candy
        i += 1
    if a_to_e == k_to_o:
        print("You Won..!!")
        solution_path = ""
        while current_node.get_node_parent():
            solution_path += current_node.get_node_name()
            current_node = current_node.get_node_parent()
        print(solution_path[::-1])
        # output_file = open("output.txt", "a+")
        output_file.write(solution_path[::-1] + "\n")
        all_solution_path += len(solution_path)
        return True
    else:
        return False


def count_heuristic():
    counter = 0
    if tileA.get_candy_value() != tileK.get_candy_value():
        counter += 1
    if tileB.get_candy_value() != tileL.get_candy_value():
        counter += 1
    if tileC.get_candy_value() != tileM.get_candy_value():
        counter += 1
    if tileD.get_candy_value() != tileN.get_candy_value():
        counter += 1
    if tileE.get_candy_value() != tileO.get_candy_value():
        counter += 1

    return counter


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


def create_child_node(current_node):
    # print(current_node.get_node_candy_setup())
    candy_setup = current_node.get_node_candy_setup()
    # Create object per each Tile.
    tileA.set_candy_value(candy_setup[0])
    tileB.set_candy_value(candy_setup[1])
    tileC.set_candy_value(candy_setup[2])
    tileD.set_candy_value(candy_setup[3])
    tileE.set_candy_value(candy_setup[4])
    tileF.set_candy_value(candy_setup[5])
    tileG.set_candy_value(candy_setup[6])
    tileH.set_candy_value(candy_setup[7])
    tileI.set_candy_value(candy_setup[8])
    tileJ.set_candy_value(candy_setup[9])
    tileK.set_candy_value(candy_setup[10])
    tileL.set_candy_value(candy_setup[11])
    tileM.set_candy_value(candy_setup[12])
    tileN.set_candy_value(candy_setup[13])
    tileO.set_candy_value(candy_setup[14])

    for tile_object_1 in tile_object_lst:
        if tile_object_1.get_candy_value() == "e":
            empty_tile = tile_object_1
            break

    # possible_moves = []
    possible_moves = empty_tile.get_possible_moves()[:]
    if current_node.previous_move == "L" or current_node.previous_move == "l":
        if "R" in possible_moves:
            possible_moves.remove("R")
    elif current_node.previous_move == "R" or current_node.previous_move == "r":
        if "L" in possible_moves:
            possible_moves.remove("L")
    elif current_node.previous_move == "U" or current_node.previous_move == "u":
        if "D" in possible_moves:
            possible_moves.remove("D")
    elif current_node.previous_move == "D" or current_node.previous_move == "d":
        if "U" in possible_moves:
            possible_moves.remove("U")

    # print(possible_moves)

    for possible_move in possible_moves:
        node_name, node_candy_setup, node_heuristic = move_tile(possible_move, empty_tile)
        node_parent = current_node
        child_node = GameNode(node_name, node_candy_setup, node_heuristic, node_parent, possible_move)
        open_list.append(child_node)
    # print(open_list)
    open_list.sort(key=lambda x: x.node_heuristic)


# Move candy tile if the input is valid
def move_tile(move, empty_tile):
    new_state = []

    if move == "U" or move == "u":
        neighbour_tile = empty_tile.get_candy_object_up()
        temp = neighbour_tile.get_candy_value()
        empty_tile.set_candy_value(neighbour_tile.get_candy_value())
        neighbour_tile.set_candy_value("e")
        for new_tile_object in tile_object_lst:
            new_state.append(new_tile_object.get_candy_value())
        heuristic = count_heuristic()
        node_name = neighbour_tile.get_tile_name()
        # empty_tile = neighbour_tile
        empty_tile.set_candy_value("e")
        neighbour_tile.set_candy_value(temp)
    elif move == "D" or move == "d":
        neighbour_tile = empty_tile.get_candy_object_down()
        temp = neighbour_tile.get_candy_value()
        empty_tile.set_candy_value(neighbour_tile.get_candy_value())
        neighbour_tile.set_candy_value("e")
        node_name = neighbour_tile.get_tile_name()
        # empty_tile = neighbour_tile
        for new_tile_object in tile_object_lst:
            new_state.append(new_tile_object.get_candy_value())
        # empty_tile = neighbour_tile
        heuristic = count_heuristic()
        empty_tile.set_candy_value("e")
        neighbour_tile.set_candy_value(temp)
    elif move == "L" or move == "l":
        neighbour_tile = empty_tile.get_candy_object_left()
        temp = neighbour_tile.get_candy_value()
        empty_tile.set_candy_value(neighbour_tile.get_candy_value())
        neighbour_tile.set_candy_value("e")
        node_name = neighbour_tile.get_tile_name()
        # empty_tile = neighbour_tile
        for new_tile_object in tile_object_lst:
            new_state.append(new_tile_object.get_candy_value())
        # empty_tile = neighbour_tile
        heuristic = count_heuristic()
        empty_tile.set_candy_value("e")
        neighbour_tile.set_candy_value(temp)
    elif move == "R" or move == "r":
        neighbour_tile = empty_tile.get_candy_object_right()
        temp = neighbour_tile.get_candy_value()
        empty_tile.set_candy_value(neighbour_tile.get_candy_value())
        neighbour_tile.set_candy_value("e")
        node_name = neighbour_tile.get_tile_name()
        # empty_tile = neighbour_tile
        for new_tile_object in tile_object_lst:
            new_state.append(new_tile_object.get_candy_value())
        # empty_tile = neighbour_tile
        heuristic = count_heuristic()
        empty_tile.set_candy_value("e")
        neighbour_tile.set_candy_value(temp)

    return node_name, new_state, heuristic


def path_finder(initial_node):
    open_list.append(initial_node)
    # print(open_list)

    while open_list:
        current = open_list[0]
        # print(current)
        open_list.pop(0)
        # print("Open list")
        # print(open_list)
        # draw_state(current.get_node_candy_setup())
        if check_goal_state(current):
            return
        # closed_list.append(current)
        # print("closed list")
        # print(closed_list)
        create_child_node(current)


if __name__ == "__main__":
    inputs = list(open("Sample_Data.txt"))

    print("Use Following commands to move Candies.")
    print("Up : U/u")
    print("Down : D/d")
    print("Right : R/r")
    print("Left : L/l")
    output_file = open("output.txt", "w+")
    all_solution_path = 0
    # output_file.flush()
    for inp in inputs:
        start_time = timeit.default_timer()
        input_candies = []
        open_list = []
        for ip in inp:
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

        tile_object_lst = [tileA, tileB, tileC, tileD, tileE, tileF, tileG, tileH, tileI, tileJ, tileK, tileL, tileM,
                           tileN,
                           tileO]

        for tile_object in tile_object_lst:
            if tile_object.get_candy_value() == "e":
                empty_tile1 = tile_object

        initial = GameNode(empty_tile1.get_tile_name(), input_candies, count_heuristic(), None, "")
        path_finder(initial)
        output_file.write(str(round((timeit.default_timer() - start_time)*1000)) + "ms" + "\n")
    output_file.write(str(all_solution_path))