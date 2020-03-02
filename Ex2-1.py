def find_min_idx(list_number):
    n = len(list_number)
    min_idx=0
    for i in range(1,n):
        if list_number[i]<list_number[min_idx]:
            min_idx=i
    return min_idx

v= [17, 92, 18, 33, 58, 7, 33, 42]

print(v[find_min_idx(v)])