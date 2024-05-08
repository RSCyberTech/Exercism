from math import *
def score(x, y):
    val=sqrt(abs(x)**2+abs(y)**2)
    return 10 if val<=1 else 5 if val<=5 else 1 if val<=10 else 0
