def drawer(x, y):
    i = 0
    while i < x:
        j = 0
        while j < y:
            print(" --- ", end="")
            j += 1
        j = 0
        print("\n", end="")
        while j < y:
            print("|   |", end="")
            j += 1
        i += 1
        print("\n", end="")
    j = 0
    while j < y:
        print(" --- ", end="")
        j += 1


def main():
    switch = 0

    while switch != 1:
        row = int(input("Please enter row number of gameboard:"))
        col = int(input("Please enter column number of gameboard:"))
        print("This is your gameboard!")
        if type(row) == int and type(col) == int and row > 0 and col > 0:
            switch = 1
        else:
            print("Row/Column numbers should be positive integers!")

    drawer(row, col)


if __name__ == '__main__':
    main()
