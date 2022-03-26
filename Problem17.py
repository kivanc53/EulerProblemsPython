# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one
# hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


def oneTo12(value):
    case = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve"

    }
    return case[value]


def twelveTo20(value):
    case = {
        0: "",
        1: "",
        2: "twen",
        3: "thir",
        4: "for",
        5: "fif",
        6: "six",
        7: "seven",
        8: "eigh",
        9: "nine"
    }
    return case[value]


def numbers(value):
    string = ""
    if value < 13:
        string += oneTo12(value)
    elif value == 14:
        string += "fourteen"
    elif value < 20:
        string = string + twelveTo20(value % 10) + "teen"
    elif value < 100:
        string += twelveTo20(value // 10) + "ty" + oneTo12(value % 10)
    elif value < 1000:
        string = string + oneTo12(value // 100) + "hundred"
        if value % 100 != 0:
            string = string + "and"
        if value % 100 < 13:
            string += oneTo12(value % 100)
        elif value % 100 == 14:
            string += "fourteen"
        elif value % 100 < 20:
            string = string + twelveTo20(((value % 100) % 10)) + "teen"
        elif value % 100 < 100:
            string = string + twelveTo20(((value % 100) // 10)) + "ty" + oneTo12(value % 10)
    elif value == 1000:
        string += "onethousand"
    return len(string)


summary = 0
for i in range(1, 1001):
    summary += numbers(i)

print(summary)
