# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
import Metotlar


largest = 0

for x in range(999, 900, -1):
    for y in range(999, 900, -1):
        if Metotlar.isPolindrome(x * y) and (x * y) > largest:
            largest = x * y
            print(x, y)

print(largest)
