# duck typing
# this is one of the types of polymorphism
class BMW:
    def drive(self):
        print("Mil is 10")
        print("235 horses")

class Lambargini:
    def drive(self):
        print("awesome inside")
        print("comfort price")
        print("Mil is 20")
        print("400 horses")

class Car:
    def fast(self,sa):
        sa.drive()
        

sa = Lambargini()
bmw = BMW()

c1 = Car()
c2 = Car()

c1.fast(sa)
c2.fast(bmw)