# it is about Iterator
# we printed numbers 1 to 10 while using iterator
class TopTen:
    def __init__(self,x):
        self.x = x
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.x:
            n = self.num 
            self.num += 1
            return n
        else:
            raise StopIteration

x = int(input("Enter any positive number: "))
sum = TopTen(x)

for i in sum:
    print(i)