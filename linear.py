pos = -1
def search(num,n):
    for i in range(len(num)):
        if num[i] == n:
            globals()['pos'] = i
            return True 

    return False

num = [12,45,87,95,65,32,2]
n = int(input("Enter any number: "))
if search(num,n):
    print("Found at", pos)
else:
    print("Not Found")