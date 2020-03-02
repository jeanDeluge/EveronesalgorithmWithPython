def plus_sum(n):
    if int(n) <=1 :
        return 1
    return n + plus_sum(n-1)


n=input("숫자 입력")
print(plus_sum(int(n)))