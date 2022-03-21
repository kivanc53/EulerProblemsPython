# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import Metotlar


countOfPrimes = 6

for i in range(14, 105001):
    if Metotlar.isPrime(i):
        countOfPrimes += 1
        if countOfPrimes == 10001:
            print(i)
            break
