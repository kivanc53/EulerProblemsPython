import Metotlar


def isAmicableNumber(n):
    realNumber = Metotlar.sumOfDivisors(n)
    secondNumber = Metotlar.sumOfDivisors(realNumber)
    if n != realNumber and n == secondNumber:
        return n
    return 0


sum = 0
for i in range(1, 10_000):
    sum += isAmicableNumber(i)
print(sum)