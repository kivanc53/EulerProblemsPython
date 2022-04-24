count = [0] * 201
count[0] = 1
for moneyList in [1, 2, 5, 10, 20, 50, 100, 200]:
    for i in range(moneyList, 201):
        count[i] += count[i - moneyList]
print(count[200])
