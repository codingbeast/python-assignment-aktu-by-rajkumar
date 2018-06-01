#by rajkumar
class raj():
    def add(self,a,b):
        c=a+b
        return c
class rj():
    def sub(self,x,y):
        z=x-y
        return z
class multilable(raj,rj):
    pass
obj1=multilable()
print(obj1.add(5,3))
print(obj1.sub(7,2))
