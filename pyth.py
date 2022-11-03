class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        

    def __add__(self,other):
        m1 = self.m1 + other.m1 
        m2 = self.m2 + other.m2
        m3 = Student(m1,m2)
        return m3

    def __sub__(self,other):
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2 
        s3 = Student(m1,m2)
        return s3
    
    def __gt__(self,other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
       
        if r1 > r2:
            return True
        else:
            return False


std1 = Student(15,24)
std2 = Student(25,84)
m3 = std1 + std2
s3 = std1 - std2

if std1 > std2:
    print("hello")
else:
    print("Goodbye")

print(m3.m1, m3.m2)
print(s3.m1, s3.m2)
print(std1)
print(std2)