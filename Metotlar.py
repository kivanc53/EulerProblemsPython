def sumOfDigits(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num //= 10
    print(sum)


def isPrime(value):
    if value <= 1:
        return False
    elif value % 2 == 0:
        return value == 2
    elif value % 3 == 0:
        return value == 3
    elif value % 5 == 0:
        return value == 5
    elif value % 7 == 0:
        return value == 7
    elif value % 11 == 0:
        return value == 11
    elif value % 13 == 0:
        return value == 13
    i = 13
    while i * i <= value:
        if value % i == 0:
            return False
        i += 2
    return True


def isPolindrome(value):
    if value == getReverse(value):
        return True
    return False


def getReverse(value):
    newValue = 0
    while value != 0:
        newValue = newValue * 10 + value % 10
        value //= 10
    return newValue


def sumOfDivisors(value):
    sum = 0
    for i in range(1, (value // 2 + 1)):
        if value % i == 0:
            sum += i
    return sum

