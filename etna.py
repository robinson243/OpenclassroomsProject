import math

def traingle(n):
    # i = 1
    # while i <= n:
    #     print('*'*i)
    #     i= i +1

    for i in range(n):
        print("+" + '*'* (i+1) + "+")

traingle(3)