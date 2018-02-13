# Uses python3


def draw_state():
    i = 0
    print("\n")
    for ic in input_candies:
        if ic == "e":
            print(" ",end="      ")
        else:
            print(ic, end="      ")
        i += 1
        if i == 5:
            i = 0
            print("\n")


if __name__ == "__main__":
    lst = list(open("Sample_Data.txt"))
    for l in lst:
        input_candies = []
        for ip in l:
            if ip != " ":
                input_candies.append(ip)
        draw_state()
