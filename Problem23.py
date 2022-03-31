import Metotlar

limit = 28124

listOfAbundantNumbers = []
sumOfAbundantNumbers = []

for i in range(12, limit):
    if Metotlar.sumOfDivisors(i) > i:
        listOfAbundantNumbers.append(i)

for k in range(0, len(listOfAbundantNumbers)):
    for j in range(k, len(listOfAbundantNumbers)):
        sumOf2Abundant = listOfAbundantNumbers[k] + listOfAbundantNumbers[j]
        if sumOf2Abundant < limit:
            sumOfAbundantNumbers.append(sumOf2Abundant)

toplam = 0
for o in range(1, limit):
    if (sumOfAbundantNumbers.__contains__(o)) == False:
        toplam += o

print(toplam)
