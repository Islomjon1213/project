def sort(num):
    for i in range(len(num)-1):
        minpos = i
        for j in range(i, len(num)):
            if num[j] < num[minpos]:
                minpos = j

        temp = num[i]
        num[i] = num[minpos]
        num[minpos] = temp

num = [12,1,54,78,2,-7,98]
sort(num)
print(num)