pos = -1


def search(num,n):
    l = 0
    u = len(num) - 1
    while l <= u:
        mid = (l+u) // 2
        if num[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if num[mid] < n:
                l = mid + 1
            else:
                u = mid - 1

    return False


num = [12,14,58,95,99]
n = int(input("Enter number you want: "))
if search(num,n):
    print("Found", pos + 1)
else:
    print("not Found")