from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass 

class Laptop(Computer):
    def process(self):
        print("It is running")

class Whiteboard(Computer):
    def process(self):
        print("it is writing")

class Programmer:
    def work(self,com):
        print("Solving bugs")
        com.process()
        


# com1 = Computer()
lap1 = Laptop()

prog1 = Programmer()
prog2 = Programmer()

wr1 = Whiteboard()
prog1.work(wr1)
prog2.work(lap1)
