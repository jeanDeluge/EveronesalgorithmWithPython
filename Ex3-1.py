#짝 만들기
def pairs(people_set):
    n=len(people_set)
    for i in range(0, n):
        for j in range(i+1, n-1):
            if people_set[i]!= people_set[j]:
                print(people_set[i]+"-"+people_set[j])
names = ["Tom", "Harry", "Belatrix", "Molly", "Sirius", "Fred", "George"]
pairs(names)

