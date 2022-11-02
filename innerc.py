# class inside the class 
# to create class inside the class
class Student:
    def __init__(self):
        self.name = "Islomjon"
        self.age = 23
        self.lap = self.Laptop()
        self.car = self.Car()
    
    def show(self):
        print(self.name, self.age)
        self.lap.show()
        self.car.show1()


    class Laptop:
        def  __init__(self):
            self.ram = 16
            self.brand = "MSI"
            self.herz = 3.70

        def show(self):
            print(self.ram, self.brand, self.herz)

    class Car:
        def __init__(self):
            self.year = 2014
            self.mil = 9
            self.name = "BMW"

        def show1(self):
            print(self.year, self.mil, self.name)
    
std1 = Student()
std2 = Student()

std1.show()
std2.show()

# lap1 = Student.Laptop()
# car1 = Student.Car()

