import math


def fifthPowersOfDigits(val):
    sum = 0
    temp = val

    while val != 0:
        sum += math.pow(val % 10, 5)
        val //= 10

    if sum == temp:
        return True
    return False


sumOfNumbers = 0

for i in range(2, 350000):
    if fifthPowersOfDigits(i):
        sumOfNumbers += i
print(sumOfNumbers)
