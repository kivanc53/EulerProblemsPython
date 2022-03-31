#dosya yolları.
laptop = "C:\\Users\\atmaca53\\OneDrive\\Euler Problemleri\\p022_names.txt"
ev = "C:\\Users\\MSI\\OneDrive\\Euler Problemleri\\p022_names.txt"

#dosya okundu
f = open(ev, "r") #r reading anlamındadır.
if f.mode == 'r':
    contents = f.read()

liste = contents.split(',')
liste.sort()

sum = 0
largest = 0
for i in range(liste.__len__()):
    for k in range(liste[i].__len__()):
        sum = sum + (ord(liste[i][k]) - 64)
    largest = largest + (sum * (i + 1))
    sum = 0

print(largest)



