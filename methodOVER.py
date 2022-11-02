# this is an axample of method everloading
class A:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def add(self,a=None,b=None,c=None):
        s = 0
        if a!= None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a
        return s


a1 = A(36,47)
print(a1.add(12))