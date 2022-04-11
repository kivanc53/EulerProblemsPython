import math


limit = 1001
sum = 1
for i in range(3, limit + 2, 2):
    sum += (4 * math.pow(i, 2)) - (6 * i) + 6
print(sum)