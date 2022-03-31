from itertools import permutations

permütasyonSeçenekleri = list(permutations('0123456789'))
sorted(permütasyonSeçenekleri)

index = 1000000 - 1
for k in range(permütasyonSeçenekleri[index].__len__()):
    print(ord(permütasyonSeçenekleri[index][k]) - 48, end = "")

