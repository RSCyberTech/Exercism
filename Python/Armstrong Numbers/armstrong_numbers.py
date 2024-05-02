def is_armstrong_number(number):
    strVersion=str(number)
    lenStr=len(strVersion)
    return sum([int(el)**lenStr for el in strVersion])==number
