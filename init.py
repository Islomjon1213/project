# create init method
# create comparing

class Students:
    def __init__(self):
        self.name = "Islomjon"
        self.age = 23
    
    # a.compare(b)
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


std1 = Students()
std2 = Students()
std2.age = 30

if std1.compare(std2):
    print("They are the same")
else:
    print("They are different")


print(std1.name, std1.age)
print(std2.name, std2.age)