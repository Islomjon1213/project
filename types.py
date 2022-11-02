# types of variables
# there are 2 types of variables
# first is Instance and second is Class variables
class Cats:

    # this is class variable
    weight = 15

    def __init__(self):
        # this is instance variable
        self.color = "black"
        self.age = 2

c1 = Cats()
c2 = Cats()

c1.age = 3
c2.color = "white"

Cats.weight = 20

print(c1.color, c1.age, c1.weight)
print(c2.color, c2.age, c2.weight)