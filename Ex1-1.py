import math

def sumOfcube(n):
    sum = 0
    for i in range(1, n+1):
        sum += math.pow(i, 2)
    return int(sum)

n = input("n을 입력하시오")

print(sumOfcube(int(n)))


def sumOfcubeO1(n):
    sum = (n*(n+1)*(2*n+1))/6
    return sum