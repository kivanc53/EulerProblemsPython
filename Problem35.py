import Metotlar
import math


def arrayToNumber(array):
    value = 0
    for b in range(0, len(array)):
        value += (array[b] * int(math.pow(10, len(array) - 1 - b)))
    return value


def checkZero(n):
    while n != 0:
        if n % 10 == 0:
            return False
        n //= 10
    return True


def numberToArray(n):
    array = []
    for ü in range(0, Metotlar.countsOfDigit(n)):
        array.append(0)
    for v in range(Metotlar.countsOfDigit(n) - 1, -1, -1):
        array[v] = n % 10
        n //= 10
    return array


def rotateArrayTo1Left(array):
    temp = array[0]
    for j in range(0, len(array) - 1):
        array[j] = array[j + 1]
    array[len(array) - 1] = temp
    return array


def isCircularPrime(n):
    if n < 100:
        return Metotlar.isPrime(Metotlar.getReverse(n))
    else:
        if checkZero(n) == False:
            return False
        else:
            temp = n
            for k in range(0, Metotlar.countsOfDigit(n) - 1):
                if Metotlar.isPrime(arrayToNumber(rotateArrayTo1Left(numberToArray(temp)))):
                    temp = arrayToNumber(rotateArrayTo1Left(numberToArray(temp)))
                else:
                    return False
        return True


count = 1
for i in range(3, 1000000, 2):
    if Metotlar.isPrime(i):
        if isCircularPrime(i):
            count += 1
print(count)
