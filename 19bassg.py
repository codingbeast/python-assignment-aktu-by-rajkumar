#by rajkumar
class rj1(object):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def sum(self):
        self.b+self.c
class rj2(object):
    def __init__(self,d,e):
        self.d=d
        self.e=e
        self.rj1=rj1('rj',1,2)
    def alsum(self):
        x=self.d+self.e+self.rj1.b+self.rj1.c
        return x
obj2=rj2(3,4)
print(obj2.alsum())
#comppsition
