import math

number = input("Karenin bir kenarını giriniz: ")
pay = math.factorial((2 * int(number)))
payda = math.factorial(int(number)) * math.factorial(int(number))

print(pay // payda)
