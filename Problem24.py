from itertools import permutations

permutationOptions = list(permutations('0123456789'))
sorted(permutationOptions)

index = 1000000 - 1
for k in range(permutationOptions[index].__len__()):
    print(ord(permutationOptions[index][k]) - 48, end="")

