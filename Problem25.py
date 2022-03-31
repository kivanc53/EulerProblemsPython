import Metotlar


firstValue = 1
secondValue = 1

for i in range(3, 5000):
    temp = secondValue
    secondValue = secondValue + firstValue
    firstValue = temp
    if Metotlar.sumOfDigits(secondValue) >= 1000:
        print(i)
        break
