def makeCollatz(value, count):

    if value == 1:
        count += 1
        return count
    elif value % 2 == 0:
        count += 1
        count = makeCollatz((value // 2), count)
        return count
    else:
        count += 1
        count = makeCollatz((3 * value + 1), count)
        return count


largest = 0
temp = 0
for i in range(13, 1_000_000):
    count = makeCollatz(i, 0)
    if count > largest:
        largest = count
        temp = i
print(temp)
