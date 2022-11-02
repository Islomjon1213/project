def sort(num):
    for i in range(len(num)-1, 0, -1):
        for j in  range(i):
            if num[j] > num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp 

num = [1,25,74,54,2,98,5,36,21,12]
sort(num)
print(num)
