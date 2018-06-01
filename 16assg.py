#by rajkumar
class raj():
    @staticmethod
    def pk():
        print("hello world")
    @classmethod
    def lk(cls,name):
        raj.myname=name
        print("nice to meet u",raj.myname)

raj.pk()
raj.lk('rajkumar')
