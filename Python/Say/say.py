def say(number):
    number_words = {
        0: "zero",
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
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }
    divisors = {
        100: "hundred",
        1000: "thousand",
        1000000: "million",
        1000000000: "billion",
    }

    if number > 0 and number <= 999_999_999_999:
        output = ""
        for v in sorted(list(divisors.keys()), reverse=True):
            if number > 0 and number // v > 0:
                output += say(number // v) + " " + divisors[v] + " "
                number -= number // v * v
        for n in sorted(list(number_words.keys()), reverse=True):
            if number > 0 and number // n > 0:
                output += number_words[n]
                if n > 19 and number % n > 0:
                    output += "-"
                number -= n
        return output.strip()
    elif number == 0:
        return "zero"
    else:
        raise ValueError("input out of range")
