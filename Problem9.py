def checkSquare(val1, val2, val3):
    if val1 + val2 + val3 == 1000 and val2 > val1 and val1 * val1 + val2 * val2 == val3 * val3:
        print(val1, "'2 + ", val2, "'2 = ", val3, "'2")
        print(val1, " * ", val2, " * ", val3, " = ", val1 * val2 * val3)
        return True
    return False


for i in range(1, 1000):
    for k in range(2, 1000):
        for j in range(3, 1000):
            if checkSquare(i, k, j):
                exit()
