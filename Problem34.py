import Metotlar


def check(value):
    sum = 0
    while value != 0:
        sum += Metotlar.factorial(value % 10)
        value //= 10
    return sum


def checkCurious(val):
    return val == check(val)


result = 0
for i in range(3, 1000000):
    if checkCurious(i):
        result += i
print(result)
