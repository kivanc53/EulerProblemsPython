import math


def addingTolist(limit):
    list = []
    for i in range(2, limit + 1):
        for k in range(2, limit + 1):
            list.append(math.pow(i, k))

    list = set(list)
    print(list)
    print(len(list))


addingTolist(100)
