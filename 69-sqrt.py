import math

## inefficient solution:
def mySqrt(x):
        lowLimit = 0

        for i in range(0, x):
            if i * i < x:
                lowLimit = i
            if i * i == x:
                lowLimit = i
        return lowLimit

## prime factorization solution?
def altSqrt(x):
    low = 0
    high = x
    while low < high:
        mid = (low + high + 1) >> 1
        if mid <= x // mid:
            low = mid
        else:
            high = mid - 1
        # print(f"low: {low}, high: {high}, mid: {mid}")
    return low

altSqrt(65)

