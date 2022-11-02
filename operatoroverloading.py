# this is eemple of operator overloading
# we can add or subctract and others while using methods __add__() and __sub__() and so on
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
 
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3
    
    def __sub__(self,other):
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2
        r3 = Student(m1,m2)
        return r3

    def __mul__(self,other):
        m1 = self.m1 * other.m1
        m2 = self.m2 * other.m2
        r4 = Student(m1,m2)
        return r4

    def __gt__(self, other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        if s1>s2:
            return True
        else:
            return False

    def __ge__(self, other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        if s1>=s2:
            return True
        else:
            return False
    
    def __str__(self):
        return "{} {}".format(self.m1, self.m2)

std1 = Student(68,42)
std2 = Student(55,35)

s3 = std1 + std2

r3 = std1 - std2

r4 = std1 * std2

print(s3.m1, s3.m2)
print(r3.m1, r3.m2)
print(r4.m1, r4.m2)

if std1 > std2:
    print("std1 wins")
else:
    print("std2 wins")

if std1 <= std2:
    print("Std2 wins")
else:
    print("LOSER")

print(std1)
print(std2)