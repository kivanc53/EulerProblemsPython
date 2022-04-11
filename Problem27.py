import Metotlar


def find(a, b):
    n = 2
    methodCount = 0
    while True:
        result = abs(n * n + a * n + b)
        if Metotlar.isPrime(result):
            methodCount += 1
        else:
            return methodCount
        n += 1


count = 0
max = 0
temp = 0
for i in range(-999, 1000, 2):
    for k in range(3, 1000, 2):
        count = find(i, k)
        if count > max:
            max = count
            temp = i * k


print(temp)