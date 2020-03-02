def find_max(listOfnumbers,n): #숫자 리스트 중 앞에서 n개까지 비교
    if n <=1 :
        return listOfnumbers[0]
    maxValue = find_max(listOfnumbers,n-1)
    if maxValue>listOfnumbers[n-1]:
        return maxValue
    else:
        return listOfnumbers[n-1]

l = [1, 3, 40, 42, 21, 20, 32]

n=input("숫자를 1~{0}사이 입력".format(len(l)))
print(find_max(l, n))

