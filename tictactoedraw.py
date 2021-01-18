import numpy as np
from Examples import Ex26CheckTicTacToe as CheckFunc


def main():
    board = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]], dtype=object)
    endCheck = 0
    counter = 0

    while endCheck == 0:
        txt = "----- Player {} Move -----"
        print(txt.format((counter % 2) + 1))
        usrInp = input("Please enter your move as 'row, column' format:")
        if ',' not in usrInp:
            raise Exception("Please enter 'row, column' format correctly")
        
        usrInp = usrInp.split(',')
        newList = []

        for i in usrInp:
            i = i.strip()
            newList.append(i)

        if newList.__len__() != 2:
            raise Exception("Please enter two numbers!")

        if board[int(newList[0])-1, int(newList[1])-1] != int("0"):
            raise Exception("Please select your move correctly!")

        if counter % 2 == 0:
            board[int(newList[0])-1, int(newList[1])-1] = "X"
        else:
            board[int(newList[0])-1, int(newList[1])-1] = "O"

        counter += 1
        checker = CheckFunc.main(board)
        if checker == []:
            pass
        else:
            endCheck = 1

            if checker == "X":
                player = 1
            elif checker == "O":
                player = 2

            print("And the winner is Player {}.".format(player))

        print(board)


if __name__ == '__main__':
    main()








