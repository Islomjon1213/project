# this is about inheritance 
# we can print sup while using sub in inheritance
class A:
    def __init__(self):
        print("A in init")

class B:
    def __init__(self):
        super().__init__()
        print("B is init")

class C(B,A):
    def __init__(self):
        super().__init__()
        print("C is init")

a1 = C()