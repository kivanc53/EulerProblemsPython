def check(num, liste):
    for q in range(1, 10):
        for w in range(1000, 10_000):
            if q * w == num:
                if check2(w, q, liste):
                    return True
                else:
                    break
    for r in range(10, 100):
        for t in range(100, 1000):
            if r * t == num:
                if check2(r, t, liste):
                    return True
                else:
                    break
    return False


def check2(num, h, arraylist):
    tempList = []
    for t in range(len(arraylist)):
        tempList.append(arraylist.__getitem__(t))
    while num != 0:
        c = num % 10
        if tempList.__contains__(c) or c < 1:
            return False
        else:
            tempList.append(c)
        num //= 10
    while h != 0:
        g = h % 10
        if tempList.__contains__(g) or g < 1:
            return False
        else:
            tempList.append(g)
        h //= 10
    return True


def isPandigital(val):
    ArrayList = []
    temp = val
    while val != 0:
        x = val % 10
        if ArrayList.__contains__(x) or x < 1:
            return False
        else:
            ArrayList.append(x)
        val //= 10
    return check(temp, ArrayList)


toplam = 0
for i in range(1000, 1_000_00):
    if isPandigital(i):
        toplam += i
print(toplam)
