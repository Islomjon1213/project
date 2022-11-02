def TopTen(x):
    n = 1
    while n <= x:
        sqr = n*n
        yield sqr 
        n += 1

x = int(input("Enter any positive number: "))
val = TopTen(x)
for i in val:
    print(i)
