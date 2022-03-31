import math


def factors(n):
    counter = 0
    k = int(math.sqrt(n))
    for i in range(1, k+1):
        if n % i == 0:
            counter += 1
    return counter * 2


sum = 0
for i in range(1, 80000000):
    sum += i
    if factors(sum) > 500:
        print(sum)
        break
