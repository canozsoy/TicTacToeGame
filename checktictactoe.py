def decider(x):
    row = x.__len__()
    col = x[0].__len__()
    y = []
    for i in range(0, row):
        if x[i, 0] == x[i, 1] and x[i, 0] == x[i, 2] and x[i, 0] != 0:
            y = x[i, 0]
            break
    for i in range(0, col):
        if x[0, i] == x[1, i] and x[0, i] == x[2, i] and x[0, i] != 0:
            y = x[0, i]
            break
    if x[0, 0] == x[1, 1] and x[0, 0] == x[2, 2] and x[0, 0] != 0:
        y = x[0, 0]
    if x[0, 2] == x[1, 1] and x[0, 2] == x[2, 0] and x[0, 2] != 0:
        y = x[0, 2]
    return y


def main(score):
    result = decider(score)
    return result


if __name__ == '__main__':
    main()

            



