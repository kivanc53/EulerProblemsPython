import Metotlar


sumOfPrimes = 0
for i in range(2, 2_000_000):
    if Metotlar.isPrime(i):
        sumOfPrimes += i
print(sumOfPrimes)
