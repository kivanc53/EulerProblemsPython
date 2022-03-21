# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

count = 1
for x in range(2520, 233_000_000, 210):
    for y in range(2, 21):
        if x % y == 0:
            count += 1
            if count == 20:
                print(x)
                break
        else:
            count = 1
            break
