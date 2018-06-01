#by rajkumar
class raj():
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
        self.both=self.name+self.addr
        print("constr is called now ")
obj=raj('rajkumar','gitm')
obj1=raj('rj','pklk')
print(obj.name)
print(obj1.addr)
print(obj.both)
