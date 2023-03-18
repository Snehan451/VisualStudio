#inside the constructor 
class Teststaticvar:
    a=10
    def __init__(self):
        Teststaticvar.b=20
    def m1(self):
        Teststaticvar.c=30
    @classmethod
    def m2(cls):
        cls.d1=40
        Teststaticvar.d2=500
    @staticmethod
    def m3():
        Teststaticvar.e=50

print(Teststaticvar.__dict__)

t=Teststaticvar()
t.m1()
print(Teststaticvar.__dict__)
t.m2()
print(Teststaticvar.__dict__)
t.m3()
print(Teststaticvar.__dict__)
t.m2()
del cls.d1
print(Teststaticvar.__dict__)
