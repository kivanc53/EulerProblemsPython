def ikiSayınınOrtakBöleni(a, b):
    if a == 0:
        return b

    return ikiSayınınOrtakBöleni(b % a, a)


payda = 1
pay = 1

for i in range(1, 10):
    for pyd in range(1, i):
        for p in range(1, pyd):
            if (p * 10 + i) * pyd == p * (i * 10 + pyd):
                payda *= pyd
                pay *= p

payda //= ikiSayınınOrtakBöleni(pay, payda)
print(payda)